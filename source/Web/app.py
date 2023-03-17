from flask import Flask, redirect, url_for, render_template, request
import model
import data_preprocessing
import pandas as pd
import numpy as np
import math
app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/predict',methods=["POST","GET"])
def model_XGB():
    pH_value = request.form["phvalue"]
    Hardness_value = request.form["hardness"]
    Solids_value = request.form["solids"]
    Chloramines_value = request.form["chloramines"]
    Sulfate_value = request.form["sulfate"]
    Conductivity_value = request.form["conductivity"]
    Organic_carbon_value = request.form["organic_carbon"]
    Trihalomethanes_value = request.form["trihalomethanes"]
    Turbidity_value = request.form["turbidity"]
    # Data Preprocessing --> missing value
    if not pH_value:
        pH_value = data_preprocessing.data_loc['ph'].mean()
    if not Hardness_value:
        Hardness_value = data_preprocessing.data_loc['Hardness'].mean()
    if not Solids_value:
        Solids_value = data_preprocessing.data_loc['Solids'].mean()
    if not Chloramines_value:
        Chloramines_value = data_preprocessing.data_loc['Chloramines'].mean()
    if not Sulfate_value:
        Sulfate_value = data_preprocessing.data_loc['Sulfate'].mean()
    if not Conductivity_value:
        Conductivity_value = data_preprocessing.data_loc['Conductivity'].mean()
    if not Organic_carbon_value:
        Organic_carbon_value = data_preprocessing.data_loc['Organic_carbon'].mean()
    if not Trihalomethanes_value:
        Trihalomethanes_value = data_preprocessing.data_loc['Trihalomethanes'].mean()
    if not Turbidity_value:
        Turbidity_value = data_preprocessing.data_loc['Turbidity'].mean()
    # Data Preprocessing --> Create DataFrame   
    x = {"ph":pH_value,"Hardness":Hardness_value,"Solids":Solids_value,"Chloramines":Chloramines_value,
        "Sulfate":Sulfate_value ,"Conductivity":Conductivity_value,"Organic_carbon":Organic_carbon_value,
        "Trihalomethanes":Trihalomethanes_value,"Turbidity":Turbidity_value
    }
    x_data = pd.DataFrame(data=x,index=[0],dtype=np.float64)
    data_loc = data_preprocessing.data_loc
    # Data Preprocessing --> Standardized Data : MinMaxScale (x - min)/(max-min)
    # PH
    x_data['ph'] = (x_data['ph'] - data_loc['ph'].min() ) / (data_loc['ph'].max() - data_loc['ph'].min())
    # Hardness
    x_data['Hardness'] = (x_data['Hardness'] - data_loc['Hardness'].min() ) / (data_loc['Hardness'].max() - data_loc['Hardness'].min())
    # Solids
    x_data['Solids'] = (x_data['Solids'] - data_loc['Solids'].min() ) / (data_loc['Solids'].max() - data_loc['Solids'].min())
    # Chloramines
    x_data['Chloramines'] = (x_data['Chloramines'] - data_loc['Chloramines'].min() ) / (data_loc['Chloramines'].max() - data_loc['Chloramines'].min())
    # Sulfate
    x_data['Sulfate'] = (x_data['Sulfate'] - data_loc['Sulfate'].min() ) / (data_loc['Sulfate'].max() - data_loc['Sulfate'].min())
    # Conductivity
    x_data['Conductivity'] = (x_data['Conductivity'] - data_loc['Conductivity'].min() ) / (data_loc['Conductivity'].max() - data_loc['Conductivity'].min())
    # Organic_carbon
    x_data['Organic_carbon'] = (x_data['Organic_carbon'] - data_loc['Organic_carbon'].min() ) / (data_loc['Organic_carbon'].max() - data_loc['Organic_carbon'].min())
    # Trihalomethanes
    x_data['Trihalomethanes'] = (x_data['Trihalomethanes'] - data_loc['Trihalomethanes'].min() ) / (data_loc['Trihalomethanes'].max() - data_loc['Trihalomethanes'].min())
    # Turbidity
    x_data['Turbidity'] = (x_data['Turbidity'] - data_loc['Turbidity'].min() ) / (data_loc['Turbidity'].max() - data_loc['Turbidity'].min())


    # Predict 
    predict_value = model.predict(x_data)
    print(predict_value)
    return render_template('index.html',predicted = predict_value[0])

if __name__ == '__main__':
    app.run(debug=True)