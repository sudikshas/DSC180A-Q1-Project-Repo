
# Importing libraries
import pandas as pd
import numpy as np
import os
import re
import gzip
from scipy.stats import percentileofscore
import shutil
import subprocess as sp
import requests
import json
import skimage.io as io
from pycocotools.coco import COCO


def extract_COCO_data(dataDir, dataFile):
    annFile='{}/annotations/instances_{}.json'.format(dataDir,dataFile)
    coco=COCO(annFile)
    return coco

def get_input_image(dataDir, dataFile, cats):
    annFile='{}/annotations/instances_{}.json'.format(dataDir,dataFile)
    coco=COCO(annFile)
    print("cats: ", cats)
    catIds = coco.getCatIds(catNms=cats)
    imgIds = coco.getImgIds(catIds=catIds)
    img = coco.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]
    img = io.imread(img['coco_url'])
#     print("type: ", type(img))
#     print('img: ', img)
    return img
    #return coco


# def get_categoriesIds(cocoObject, cats):
#     # annFile='{}/annotations/instances_{}.json'.format(dataDir,dataFile)
#     # coco=COCO(annFile)
#     #cats = coco.loadCats(coco.getCatIds())
#     catIds = cocoObject.getCatIds(catNms=cats)
#     return catIds

    #imgIds = coco.getImgIds(catIds=catIds)

    
    # catIds2 = coco.getCatIds(catNms=base+added)
    # imgIds2 = coco.getImgIds(catIds=catIds2)
    #return catIds

def get_imageIds(cocoObject, catIds):
    return cocoObject.getImgIds(catIds=catIds)