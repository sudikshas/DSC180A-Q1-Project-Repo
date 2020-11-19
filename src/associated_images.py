
from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import sys
import json


# dataDir='..'
# dataType='val2017'

# annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)
# coco=COCO(annFile)
# cats = coco.loadCats(coco.getCatIds())
def get_associated_objects_images(cocoObject, imgIds1, imgIds2, base, added):
    #impath = '../images'
    #lst = []
    # annFile='{}/annotations/instances_{}.json'.format(dataDir,dataFile)
    # coco=COCO(annFile)
    # #cats = coco.loadCats(coco.getCatIds())
    # catIds = coco.getCatIds(catNms=base)
    # imgIds = coco.getImgIds(catIds=catIds)
    
    # catIds2 = coco.getCatIds(catNms=base+added)
    # imgIds2 = coco.getImgIds(catIds=catIds2)

    perc = len(imgIds2)/len(imgIds1) * 100
    
    summary =  "{}% of the images with {} have {}".format(perc,', '.join(base),
                                                          ', '.join(added))
    for i in imgIds2:
        img = cocoObject.loadImgs(i)[0]
        I=io.imread(img['coco_url'])
        plt.axis('off')
        ax= plt.imshow(I)
        plt.imsave('../images/'+str(i)+'.png', I) 
        plt.show(ax)
    print(summary)
    return summary