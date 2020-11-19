#!usr/bin/env pyhton
#%matplotlib inline
from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import sys
import json
#pylab.rcParams['figure.figsize'] = (8.0, 10.0)

dataDir='..'
dataType='val2017'

annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)
coco=COCO(annFile)
cats = coco.loadCats(coco.getCatIds())
#nms=[cat['name'] for cat in cats]
#print('COCO categories: \n{}\n'.format(' '.join(nms)))

#nms = set([cat['supercategory'] for cat in cats])
#print('COCO supercategories: \n{}'.format(' '.join(nms)))
#catIds = coco.getCatIds(catNms=['car','dog']);
#imgIds = coco.getImgIds(catIds=catIds);
#print(len(imgIds))
#print(imgIds)

annFile = '{}/annotations/captions_{}.json'.format(dataDir,dataType)
coco_caps=COCO(annFile)
def get_associated_objects_images(base, added):
    impath = '../images'
    #lst = []
    catIds = coco.getCatIds(catNms=base);
    imgIds = coco.getImgIds(catIds=catIds);
    
    catIds2 = coco.getCatIds(catNms=base+added);
    imgIds2 = coco.getImgIds(catIds=catIds2);
    perc = len(imgIds2)/len(imgIds) * 100
    
    summary =  "{}% of the images with {} have {}".format(perc,', '.join(base_objects),
                                                          ', '.join(add_objects))
    for i in imgIds2:
        img = coco.loadImgs(i)[0]
        I=io.imread(img['coco_url'])
        plt.axis('off')
        ax= plt.imshow(I)
        plt.imsave('../images/'+str(i)+'.png', I) 
        plt.show(ax)
    print(summary)
    return summary



with open('data_params.json') as f:
    data = json.load(f)
base_objects=[]
add_objects=[]
for i in data['base_objects']: 
    base_objects.append(i)
for i in data['add_objects']:
    add_objects.append(i)
print("RESULTS PRINTED IN ExplainableAI_checkpoint1/images")
get_associated_objects_images(base_objects, add_objects)    
