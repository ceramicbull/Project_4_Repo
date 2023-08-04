import numpy as np
import os
import pandas as pd
from flask import Flask, request, render_template
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

# load model
model = tf.keras.models.load_model("NN/sleep_model_opt.hdf5")

# load training data for scaling
X_train = pd.read_csv("NN/X_train.csv")

# fit scaler
scaler = StandardScaler()
input_scaler = scaler.fit(X_train)

# lists of features:
keys = ['age', 'sleep_duration', 'quality_of_sleep', 'physical_activity_level',
        'stress_level', 'heart_rate', 'daily_steps', 'systolic_blood_pressure',
        'diastolic_blood_pressure', 'Accountant', 'Doctor', 'Engineer',
        'Lawyer', 'Nurse', 'Other', 'Salesperson', 'Teacher', 'Normal Weight',
        'Overweight', 'Female', 'Male']
# keys of numerical features:
num_keys = ['age', 'sleep_duration', 'quality_of_sleep', 'physical_activity_level',
            'stress_level', 'heart_rate', 'daily_steps', 'systolic_blood_pressure',
            'diastolic_blood_pressure']
# keys for career category:
career_keys = ['Accountant', 'Doctor', 'Engineer',
               'Lawyer', 'Nurse', 'Other', 'Salesperson', 'Teacher']
# keys for BMI category:
bmi_keys = ['Normal Weight',
            'Overweight']
# keys for gender category:
gen_keys = ['Female', 'Male']


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
# create our "home" route using the "index.html" page
@app.route("/", methods=['POST', 'GET'])
def main_page():
    """
    Render the main page of the webapp.
    """

    return render_template('index.html')

# Set a post method to yield predictions on page


@app.route('/predict', methods=['POST'])
def predict():

    # obtain all form values and convert to pandas df
    data = request.form
    print(request.form)
    # convert the "ImmutableMultiDict" into a standard dict:
    input_dict = {}
    # get numerical values:
    for key in num_keys:
        input_dict[key] = data.getlist(key)[0]
    # convert to pandas df
    print(input_dict)
    input_df = pd.DataFrame(input_dict, index=[0])
    # add categorical values to DataFrame
    for key in career_keys:
        input_df[key] = [0]
    for key in bmi_keys:
        input_df[key] = [0]
    for key in gen_keys:
        input_df[key] = [0]
    print(list(input_df.columns))
    # determine career value:
    car = data.getlist('career')[0]
    print(car)
    # determine bmi value:
    bmi_ = data.getlist('bmi')[0]
    print(bmi_)
    # determine gender value:
    gen_ = data.getlist('gender')[0]
    print(gen_)
    # change selected categorical values to 1:
    cat_list = [car, bmi_, gen_]
    for cat in cat_list:
        input_df.iloc[0, input_df.columns.get_loc(cat)] = 1
    # ensure DataFrame is in correct order:
    input_df = input_df[keys]
    print(list(input_df.columns))
    print(list(input_df.iloc[0, :]))
    # scale input DataFrame:
    input_ = input_scaler.transform(input_df)
    # predict the price given the values inputted by user
    prediction = model.predict(input_)
    print(prediction)

    # prediction output:
    # if between 0 and .5, no disorder:
    if (prediction < 0.5) & (prediction >= 0):
        return "You are not likely to have a sleeping disorder."
    # if between .5 and 1, yes disorder:
    elif (prediction >= 0.5) & (prediction < 1):
        return "You may be at risk for a Sleeping Disorder."
    # otherwise, something is wrong:
    else:
        return "Uh oh. Something went wrong."


# Run app
if __name__ == "__main__":
    app.run(debug=True)
