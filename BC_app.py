import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

#load model
model=tf.keras.models.load_model("NN/sleep_model_opt.hdf5")

#load training data for scaling
X_train=pd.read_csv("NN/X_train.csv")

#fit scaler
scaler = StandardScaler()
input_scaler = scaler.fit(X_train)


#lists of features
keys=['age', 'sleep_duration', 'quality_of_sleep', 'physical_activity_level',
       'stress_level', 'heart_rate', 'daily_steps', 'systolic_blood_pressure',
       'diastolic_blood_pressure', 'Accountant', 'Doctor', 'Engineer',
       'Lawyer', 'Nurse', 'Other', 'Salesperson', 'Teacher', 'Normal Weight',
       'Overweight', 'Female', 'Male']
#keys of numerical features
num_keys=['age', 'sleep_duration', 'quality_of_sleep', 'physical_activity_level',
       'stress_level', 'heart_rate', 'daily_steps', 'systolic_blood_pressure',
       'diastolic_blood_pressure']
#cat_keys=['career','bmi','gen']
#keys for career category
career_keys=['Accountant', 'Doctor', 'Engineer',
       'Lawyer', 'Nurse', 'Other', 'Salesperson', 'Teacher']
#keys for BMI category
bmi_keys=['Normal Weight',
       'Overweight']
#keys for gender category
gen_keys=['Female', 'Male']

#example output
#ImmutableMultiDict([
#    ('age', '37'),
#    ('sleep_duration', '6'),
#    ('quality_of_sleep', '7'),
#    ('physical_activity_level', '40'),
#    ('stress_level', '6'),
#    ('heart_rate', '70'),
#    ('daily_steps', '5000'),
#    ('systolic_blood_pressure', '130'),
#    ('diastolic_blood_pressure', '80'),
#    ('career', 'Other'),
#    ('bmi', 'Overweight'),
#    ('gender', 'Male')])


#################################################
# Flask Setup
#################################################
app = Flask(__name__, template_folder = 'templates')



#################################################
# Flask Routes
#################################################
@app.route("/", methods=['POST', 'GET'])
def main_page():
    """
    Render the main page of the webapp.
    """
    
    return render_template('BC_index.html')


#Set a post method to yield predictions on page
@app.route('/predict', methods = ['POST'])
def predict():
    
    #obtain all form values and convert to pandas df
    print(request.form)
    input_df=pd.DataFrame(request.form.values())
    #ensure DataFrame is in correct order:
    input_df=input_df[keys]
    #scale DataFrame:
    input_=input_scaler.transform(input_df)
    #predict the price given the values inputted by user
    prediction = model.predict(input_)
   
    
    #If the output is negative, the values entered are unreasonable to the context of the application
    #If the output is greater than 0, return prediction
    if prediction < 0.5 & prediction>0:
        return render_template('index.html', prediction_text = "It is unlikely that you have a Sleeping Disorder.")
    elif output >= 0.5:
        return render_template('index.html', prediction_text = "It is likely that you have a Sleeping Disorder.")   
    else: 
        return render_template('index.html', prediction_text = "Uh oh. Something went wrong.")   
#Run app

if __name__ == '__main__':
    app.run(debug=True)
