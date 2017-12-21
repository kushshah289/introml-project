# introml-project

Introduction:
=============
Our project is named neural style transfer. We see on social media that people like to mix their image with different types of styles. Here we are trying to achieve the same using neural style transfer.

Flow:
=====
Here we take two images as input. One is the content image and other is the style image. Then using our model we generate a mixed image which has th contours of the content image and the colours and texture of the style image. The loss-function for the content-image tries to minimize the difference between the features that are activated for the content-image and for the mixed-image, at one or more layers in the network.

What we have done differently:
==============================
* We first learned tensorflow from: https://learningtensorflow.com/
* We then implemented the working of the code using tensorflow.
* We also used the flickr API we learned in CNN lab to generate test data. This data is stored in [texture_output](https://github.com/kushshah289/introml-project/tree/master/texture_outer/texture) file.
* We also treid to implement different optimizers like the adam optimizer but we were unable to solve the errors. This is in [trial.ipynb](https://github.com/kushshah289/introml-project/)

References:
===========
We have referred the code from here: https://github.com/Hvass-Labs/TensorFlow-Tutorials/blob/master/15_Style_Transfer.ipynb

Contributors:
=============
rcm445 nd1292 ks4437

Here, we have used the optimal setting for content-image and style-image.
=========================================================================
![alt text](https://github.com/kushshah289/introml-project/blob/master/readme%20file/1_1.PNG)
![alt text](https://github.com/kushshah289/introml-project/blob/master/readme%20file/1_2.PNG)
![alt text](https://github.com/kushshah289/introml-project/blob/master/readme%20file/1_3.PNG)<br>
Here, the weight of content-image is very high as compared to the weight of the style image.
============================================================================================
![alt text](https://github.com/kushshah289/introml-project/blob/master/readme%20file/2_1.PNG)
![alt text](https://github.com/kushshah289/introml-project/blob/master/readme%20file/2_2.PNG)
![alt text](https://github.com/kushshah289/introml-project/blob/master/readme%20file/2_3.PNG)<br>
Here, the weight of style-image is very high as compared to the weight of the content-image.
============================================================================================
![alt text](https://github.com/kushshah289/introml-project/blob/master/readme%20file/3_1.PNG)
![alt text](https://github.com/kushshah289/introml-project/blob/master/readme%20file/3_2.PNG)
![alt text](https://github.com/kushshah289/introml-project/blob/master/readme%20file/3_3.PNG)<br>
<br>
Flow Graph
==========
![alt text](https://github.com/kushshah289/introml-project/blob/master/readme%20file/graph.png)

