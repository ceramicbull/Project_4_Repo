import numpy as np

from flask import Flask, render_template

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def main_page():
    """
    Render the main page of the webapp.
    """
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
