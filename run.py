#!/usr/bin/env python

#imports
import sys
import os
import json
import os.path
import os
import cv2


from src.etl import *
#src/etl.py
#from features import apply_features


#from src import training_image_classifier
from src.grad_cam_model import run_models
from src.grad_cam import *
from src.training_image_classifier import training_classifier


#from src.associated_images import *
#from src.training_image_classifier import *


#import functions from files
sys.path.insert(0, 'src') # add library code to path


#get config file path names
data_params = 'config/data_input_params.json'
file_params = 'config/data_files.json'
results_paths = 'config/results_paths.json'
test_results = 'config/test_results_file.json'




#function to load the config files into json
def load_params(fp):
    with open(fp) as fh:
        param = json.load(fh)

    return param


#main function to run
def main(targets):
                
    #test full project; data ingestion process and visuals


    if 'generate_image' in targets: #data
        #access files for the data
        files = load_params(file_params)
        #perform etl
        img = get_input_image(files["data_dir"], files["data_file"], files["object_categories"])
        cv2.imwrite(files["image_out_path"], img)
       


    if 'test' in targets:

        results = load_params(results_paths)
        
        save_path = results["out_dir"]
        
        if not os.path.exists(save_path):
            os.makedirs(save_path) 
        print("finish making data directory")
    
        run_models(results["image_out_path"],results["cam_img"],results["gb_dir"], results['cam_dir'])
        print("finished running model")

        
    return

#first call to start data pipeline
if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)