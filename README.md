# plastic cap inspection
The project is supposed to take an image and then mark the plastic cap and measure its diameter

## _Dataset_
Due to the unavailability of the dataset, 
-  created a database with the help of images in Google

    An example image of from the dataset-Google: 
    
    ![192-1924614_bottle-caps-metal-caps-free-picture-bottle-cap](https://user-images.githubusercontent.com/79938552/131983283-ef19b2a7-ca98-4367-a8ea-87e2aecb5d52.jpg)
  
-  Data generation with data augmentation 

    An example image of from the dataset-augmentation: 
    
    ![192-1924614_bottle-caps-metal-caps-free-picture-bottle-cap](https://user-images.githubusercontent.com/79938552/131982174-d032aab3-a519-4795-874e-6d534a0f8dc9.png)
    
Finally, I prepared a database with 92 images

## _The method of project_
This project is done with Python programming language and can be run on a variety of OS, including Windows, Linux and mobile.
The speed of this project is less than 1 second
### step1: Cap Detection by YOLOV5
To us YOLO, First, we need to label images (label=cap)

An example image of from the dataset(The database is labeled): 
![download](https://user-images.githubusercontent.com/79938552/131993072-d35fdad5-74bc-4877-9b4e-b3da43ba532b.jpg)

we train YOLO with their pictures and labels. Then, after receiving each image, we first detection the plastic cap and calculate the diameter of the cap according to the size of the image.

![download](https://user-images.githubusercontent.com/79938552/131995993-aba02cec-f84e-4b03-a692-e54adb888522.png)
