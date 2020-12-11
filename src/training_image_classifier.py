


import torch
# from src import *
# from utils import (
#     get_model_instance_segmentation,
#     collate_fn,
#     get_transform,
#     myOwnDataset,
# )




print("Torch version:", torch.__version__)

def training_classifier(train_data_dir, train_coco, train_batch_size, train_shuffle_dl,num_workers_dl,
        num_classes, num_epochs, lr, momentum, weight_decay,max_num_images):

    # create own Dataset
    my_dataset = myOwnDataset(
        root=train_data_dir, annotation=train_coco, transforms=get_transform()
    )

    # own DataLoader
    data_loader = torch.utils.data.DataLoader(
        my_dataset,
        batch_size= train_batch_size,
        shuffle= train_shuffle_dl,
        num_workers= num_workers_dl,
        collate_fn=collate_fn,
    )


    # select device (whether GPU or CPU)
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

    # DataLoader is iterable over Dataset
    for imgs, annotations in data_loader:
        imgs = list(img.to(device) for img in imgs)
        annotations = [{k: v.to(device) for k, v in t.items()} for t in annotations]
        print(annotations)


    model = get_model_instance_segmentation(num_classes)

    # move model to the right device
    model.to(device)

    # parameters
    params = [p for p in model.parameters() if p.requires_grad]
    optimizer = torch.optim.SGD(
        params, lr=lr, momentum=momentum, weight_decay=weight_decay
    )

    len_dataloader = len(data_loader)

    # Training
    for epoch in range(num_epochs):
        print(f"Epoch: {epoch}/{num_epochs}")
        max_images = 0
        model.train()
        i = 0
        for imgs, annotations in data_loader:
            #i += 1
            imgs = list(img.to(device) for img in imgs)
            annotations = [{k: v.to(device) for k, v in t.items()} for t in annotations]
            loss_dict = model(imgs, annotations)
            losses = sum(loss for loss in loss_dict.values())

            optimizer.zero_grad()
            losses.backward()
            optimizer.step()


            if max_images == max_num_images:
                break
            i += 1
            max_images += 1

            print(f"Iteration: {i}/{len_dataloader}, Loss: {losses}")
    final_output = "Final training error loss is " + str(losses)
    return final_output