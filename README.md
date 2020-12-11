# DSC180A: ExplainableAI Replication Project

<!--- Quick Note: While our code runs on the dsmlp cluster, we had problems pushing to github. I have downloaded individual files such as the demo and the run file. THe run file woud need the dataset and a config folder with the uploaded data-params.json file.(For this iteration of the run file we do not need the config folder) We will need some help in Office hours to understand how to submit this for future replications of the demo  ---> 



Purpose of Our Demo Notebook:

The purpose of our demo notebook is to apply the Grad-CAM algorithm to images from the COCO dataset and to observe the generated heatmaps that show which parts of the image the model focuses on when making its object classifications. Our code has a function in which users can input categories that the image should have to observe how Grad-CAM behaves on images with multiple objects in focus. Additionally, the demo notebook shows all the images that have objects from all the inputted categories along with the three heatmaps: the class activatoin map, the guided backpropagaton heatmap, and both of those heatmaps combined on top of th einput image. 


Apart from that principle, the demonotebook along with the run script, outputs a list of images based on parameters: base_images and add_objects. These parameters can be changed for experimentation in the data-params.json file. Ths will out put a percentage based on the information above as well as images satisfying that criteria in the folder images in the main directory. This images folder will get rewritten based on changes to the data-params.json file

        How to run the demo notebook:

**python run.py generate_image**

This will create an input image that has the categories specified in the data-params.json file. It stores this resulting image in the test data folder.


**python run.py test**

This target runs the grad cam algorithm on the generated input image from the previosu target. 

Group Members Work Contributions:
- Pratyush Juneja: Worked on the final replication report and demo notebook
-Sudiksha - Worked on setting up the Grad-CAM code and applying it to COCO dataset
