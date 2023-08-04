# Lifestyle Patterns and Sleep Disorders

## Introduction
This project uses machine learning to predict the likelihood of having a sleep disorder based on lifestyle patterns and health indicators. An [artificial dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset) was used to train and test various logistic regression and neural network models to identify the model with the highest accuracy. An optimized model was selected and a webpage was created to visualize the dataset and provide an interactive form that would allow users to submit their own data into a form which would then output the likelihood of a sleep disorder based on the model's predictions.

## Data
The [artificial dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset) was cleaned and used to create a [SQLite database](https://github.com/ceramicbull/Project_4_Repo/blob/main/database_setup.py) that was used to test and train the models. 

## Models
The data was preprocessed and cleaned further for training and testing the models which include: 
- [Logistic Regression](https://github.com/ceramicbull/Project_4_Repo/tree/main/Logistic%20Regression) 
- [Decision Tree](https://github.com/ceramicbull/Project_4_Repo/tree/main/Logistic%20Regression) 
- [Random Forest](https://github.com/ceramicbull/Project_4_Repo/tree/main/Logistic%20Regression)  
- [Neural Network](https://github.com/ceramicbull/Project_4_Repo/tree/main/NN)  

## Model Optimization and Results
The logistic regression, decision tree and random forest models were evaluated by calculating an accuracy score, creating a classification report, confusion matrix and looking at the features importance. The neural network model was optimized by utilizing KerasTuner and calculating the difference between using 1 or 3 'y' categories in the model.  

The following shows the comparisons between the various models used:

![image](https://github.com/ceramicbull/Project_4_Repo/assets/120599626/4e0adf29-6cc7-4cf3-9637-e66212cf6ca5)   

After the optimization process the optimized neural network using one binary 'y' feature was selected as the best option. 

## Visualizations and Webpage
A [Tableau Dashboard](https://public.tableau.com/app/profile/chelsea.pickett7387/viz/LifestylePatternsandSleepDisorders/Dashboard2) was created to visualize the relationships between lifestyle patterns and sleep disorders in the artificial dataset and a bootstrap webpage template was used to create a user interface. An HTML form was utilized in the webpage as well. The template was personalized and stylized using bootstrap, HTMX and HTML. The optimized model was used in the flask [app.py](https://github.com/ceramicbull/Project_4_Repo/blob/main/app.py) file to connect the model to the webpage and allow user data from the webpage form to be calculated as inputs in the optimized model. The webpage then outputs the result of the model on the webpage. 

## Conclusion
The neural network model using one binary 'y' feature was determined to have the highest accuracy of the various models tested, showing a 94% accuracy in the prediction of whether or not the person would be likely to have a sleep disorder or not based on the input data provided by that person. The artificial dataset was selected for ease of use and simplicity but it is noted that using real data from a sleep study or from actual observations from the public may lead to different conclusions about lifestyle patterns and sleep disorders.

## Resources
[Sleep Health and Lifestyle Dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset)  
[Deploying Machine Learning Models Into A Website Using Flask](https://towardsdatascience.com/deploying-machine-learning-models-into-a-website-using-flask-8582b7ce8802)  
[Bootstrap Scrolling Nav Template](https://startbootstrap.com/template/scrolling-nav)  
[HTML Forms](https://www.w3schools.com/html/html_forms.asp)  

## Contributors
[Benjamin Chilcoat](https://github.com/ceramicbull)  
[Chelsea Pickett](https://github.com/chelseapickett)    
[Leigha Russell](https://github.com/lrussell834)

## Index
 [app.py](https://github.com/ceramicbull/Project_4_Repo/blob/main/app.py)  
 [Index.html](https://github.com/ceramicbull/Project_4_Repo/blob/main/templates/index.html)   
 [Logistic Regression/Decision Tree/Random Forest Models](https://github.com/ceramicbull/Project_4_Repo/tree/main/Logistic%20Regression)  - [Neural Network Models](https://github.com/ceramicbull/Project_4_Repo/tree/main/NN)      
 [Slide deck](https://docs.google.com/presentation/d/1LB59TGCeNBc9BzVj1jBBx5BR8IZXCjS_jf5XU5wd6EI/edit#slide=id.g25eabba6b9a_0_762)  
 [Source Data (cleaned)](https://github.com/ceramicbull/Project_4_Repo/blob/main/data/Sleep_health_mk1.csv)   
 [SQLite Database setup](https://github.com/ceramicbull/Project_4_Repo/blob/main/database_setup.py)  
 [Tableau Dashboard](https://public.tableau.com/app/profile/chelsea.pickett7387/viz/LifestylePatternsandSleepDisorders/Dashboard2) 
     
  


