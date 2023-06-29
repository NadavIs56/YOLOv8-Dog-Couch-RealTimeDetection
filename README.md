# YOLOv8-Dog-Couch-RealTimeDetection


#  <p align ="center" height="40px" width="40px"> Dog On Couch Detector 🐾🛋️ </p>

### <p align ="center"> Implemented using: </p>
<p align ="center">
<a href="https://www.python.org/" target="_blank" rel="noreferrer">   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png" width="32" height="32" /></a>
<a href="https://docs.ultralytics.com/" target="_blank" rel="noreferrer">   <img src="https://ultralytics.com/static/brand/yolov8-r1-1.svg" width="128" height="64" /></a>  
<a href="https://opencv.org/" target="_blank" rel="noreferrer">   <img src="https://opencv.org/wp-content/uploads/2022/05/logo.png" width="32" height="32" /></a>  



</p>
           
###     <p align = "center"> You can access the web version at https://skin-disease-ai.streamlit.app/ </p>
####     <p align = "center"> I would appreciate hearing your thoughts on it. Thank you! </p>

<br>

#### <p align = "center"> Welcome to Skin Disease AI, an advanced system designed to recognize and diagnose skin diseases using machine learning and image processing techniques. This project offers an AI solution that can significantly assist in the diagnostic process of six different types of skin lesions.</p>

<br>

##     <p align = "left"> 🎯 Introduction </p>

Skin conditions are a common reason for clinic visits, with an accurate diagnosis being crucial for effective treatment. This project presents a robust machine learning system that analyzes images to identify and diagnose different types of skin lesions.

<br>

##     <p align = "left"> 📚 Dataset </p>
The dataset for this project consists of a total of 1,952 images. These images represent six types of skin lesions, gathered from public dermatologist datasets and self-collected sources.

<br>

##     <p align = "left"> 🤖 Model </p>
We utilized the Xception architecture to create our skin lesion diagnosis model. Trained on the complete dataset, we enhanced our training with data augmentation for classes with fewer images. Our model achieved an impressive 87% accuracy on the test set. In addition, we assessed our model using various metrics, including the confusion matrix, accuracy and loss histograms, and a comprehensive classification report.

<br>

##     <p align = "left"> 📂 Repository Structure </p>
 -  'preprocessing.py': This code loads the entire dataset, perform the required image preprocessing, and splits the images into train, validation and test sets.

 -  'sets_visualization.py': This code used to show the distribution of the different skin lesions' types through the train, validation and test sets.

 -  'augmentation.py': Code for adding augmented images to our dataset for classes with a lack of images.

 -  'model.py': The code we used to build our Xception model for skin lesion diagnosis.

 -  'evaluate.py': Code for evaluating our model for fine-tuning and better understanding. It shows the confusion matrix, accuracy and loss histograms, and classification  report.

 -  'predict.py': Code for prediction a batch of images from a directory, using our model. 

<br>

### <p align ="center"> Do remember to star ⭐ the repository if you like what you see!</p>


