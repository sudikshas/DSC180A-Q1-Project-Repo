#!/usr/bin/env python

#imports
import sys
import os
import json
import os.path
import os


from src.etl import *
#src/etl.py
#from features import apply_features
from src.Model.model import build_model

#from src import training_image_classifier
from src.training_image_classifier import training_classifier
from src.associated_images import *
#from src.associated_images import *
#from src.training_image_classifier import *


#import functions from files
sys.path.insert(0, 'src') # add library code to path
# from data_ingestion import *
# from viz import *


#get config file path names
#data_ingest_params = 'config/test_data_params.json'
data_params = 'config/data_params.json'
file_params = 'config/data_files.json'
results_dir = 'config/results_file.json'
test_params = 'test/testdata/test_params.json'
test_results = 'config/test_results_file.json'
classifier_params = 'config/classifier_params.json'
#cnn_params = 'config/test_results_file.json'



#function to load the config files into json
def load_params(fp):
    with open(fp) as fh:
        param = json.load(fh)

    return param


#main function to run
def main(targets):

    # make the clean target
    # if 'clean' in targets:
    #     #shutil.rmtree('testData/', ignore_errors=True)
    #     shutil.rmtree('finalVisuals/', ignore_errors=True)
                
    #test full project; data ingestion process and visuals

    if 'association-summary' in targets:
        p = load_params(data_params)

        #access files for the data
        files = load_params(file_params)
        #perform etl
        coco = extract_COCO_data(files["data_dir"], files["data_file"])
        catsIds1 = get_categoriesIds(coco, p["base_objects"])
        catsIds2 = get_categoriesIds(coco, p["base_objects"] + p["add_objects"])

        img_Ids1 = get_imageIds(coco, catsIds1)
        img_Ids2 = get_imageIds(coco, catsIds2) 

        summary = get_associated_objects_images(coco,img_Ids1, img_Ids2, p["base_objects"], p["add_objects"])

        outFile = load_params(results_dir)["out_file"]
        outF = open(outFile, "w")
        outF.write(summary)
        outF.close()

    if "train_classifier" in targets:
        cnn_params = load_params(classifier_params)
        loss_score = training_classifier(cnn_params['train_data_dir'], cnn_params["train_coco"], cnn_params['train_batch_size'], cnn_params["train_shuffle_dl"], cnn_params["num_workers_dl"],
        cnn_params["num_classes"], cnn_params["num_epochs"], cnn_params["lr"], cnn_params["momentum"],
        cnn_params["weight_decay"], cnn_params["max_num_images"])

        

        save_path = cnn_params["result_file"]
        #completeFileName = os.path.join(save_path, "test_results.txt")         
        outFile = open(save_path, "w")
        #print(outFile)
        #outF = open(outFile, "w")
        outFile.write(loss_score)
        print("printed classifier training results")
        outFile.close()



    if 'test' in targets:
        #instances_file = 
        p = load_params(test_params)
        files = load_params(file_params)
        #perform etl
        coco = extract_COCO_data(files["data_dir"], files["data_file"])
        catsIds1 = get_categoriesIds(coco, p["base_objects"])
        catsIds2 = get_categoriesIds(coco, p["base_objects"] + p["add_objects"])

        img_Ids1 = get_imageIds(coco, catsIds1)
        img_Ids2 = get_imageIds(coco, catsIds2) 

        summary = get_associated_objects_images(coco,img_Ids1, img_Ids2, p["base_objects"], p["add_objects"])

        

        save_path = load_params(test_results)["out_file"]
        #completeFileName = os.path.join(save_path, "test_results.txt") 
        os.makedirs(os.path.dirname(save_path), exist_ok=True)        
        outFile = open(save_path, "w")
        #print(outFile)
        #outF = open(outFile, "w")
        outFile.write(summary)
        print("wrote test summary")
        outFile.close()

        # collect_data(cfg["websites"], cfg["outdir"], "test")
        
        # cfg = load_params(visuals_params)
        # create_plots(cfg["indir"], cfg["outdir"])
       
    #test full project; data ingestion process and visuals 
    # if 'run-project' in targets:
    #     cfg = load_params(data_ingest_params)
    #     collect_data(cfg["websites"], cfg["outdir"], "full")
        
    #     cfg = load_params(visuals_params) #from data ingestion
    #     create_plots(cfg["indir"], cfg["outdir"])
        
    return

#first call to start data pipeline
if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)