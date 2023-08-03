import numpy as np
import os

from flask import Flask, render_template

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
# create our "home" route using the "index.html" page
@app.route('/')
def home():
    return render_template('CP_index.html')

# Set a post method to yield predictions on page


@ app.route('/', methods=['POST'])
def predict():
    # BEN'S MODEL CODE GOES HERE
    return "Test Prediction Result Successful"


# Run app
if __name__ == "__main__":
    app.run(debug=True)
