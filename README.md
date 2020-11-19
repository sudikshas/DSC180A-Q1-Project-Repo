# ExplainableAI_checkpoint2

Quick Note: While our code runs on the dsmlp cluster, we had problems pushing to github. I have downloaded individual files such as the demo and the run file. THe run file woud need the dataset and a config folder with the uploaded data-params.json file.(For this iteration of the run file we do not need the config folder) We will need some help in Office hours to understand how to submit this for future replications of the demo 



Purpose of Our Demo Notebook:

The purpose of our demo notebook is to make some changes from the original COCO API demo notebook to explore the information we can collect using the COCO API. Our demo has a function in which users can input categories that the image should have and another list of categories could be in the image as well. The function finds all images with the first list of given categories and returns what percentage of those images also have the categories from the second list. This percentage can help us understand the relationship between objects of these categories and how common it is to see them paired together in a natural setting. Additionally, the demo notebook shows all the images that have objects from all the inputted categories along with captions to help users understand how those objects might be related to each other and there are also annotations on the image with a bounding box to show which objects in the image were identified to be a part of all the inputted categories.


Apart from that principle, the demonotebook along with the run script, outputs a list of images based on parameters: base_images and add_objects. These parameters can be changed for experimentation in the data-params.json file. Ths will out put a percentage based on the information above as well as images satisfying that criteria in the folder images in the main directory. This images folder will get rewritten based on changes to the data-params.json file

        How to run the demo notebook:

**python run.py**

This will create the images folder mentioned above as well as output the percentage of similarity between the two given parameters.


       Config/Data-params.json file:

	Contains json with the parameters: “base_images” and “add_objects”


-       base_images parameter allows users to input categories that the image needs to have

-       add_objects parameter allows users to input additional objects to check if these categories are in the images with the base images

**python run.py test**

Runs all the targets on a given test data under the test/testdata directory

Group Members Work Contributions:
- Pratyush Juneja: Worked on the run.py file t obe executed with data-params.json
-Sudiksha - Worked on intro and replicating diffrent demo
