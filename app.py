from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)

import joblib
model = joblib.load("svd_DimRed")

@app.route('/')
def home():
    return render_template('index.html')
def table():
    return render_template("table.html")

@app.route('/success', methods = ['POST'])
def success():
    if request.method == 'POST' :
        f = request.files['file']
        data = pd.read_excel(f)
        
        # Drop the unwanted features
        data1 = data.drop(["UnivID"], axis = 1)
        
        # Read only numeric data
        num_cols = data1.select_dtypes(exclude = ['object']).columns
        
        # Perform SVD using the saved model
        svd_res = pd.DataFrame(model.transform(data1[num_cols]), columns = ['svd0', 'svd1', 'svd2', 'svd3', 'svd4'])

        return render_template("data.html", Y = svd_res.to_html())

if __name__=='__main__':
    app.run(debug = True)