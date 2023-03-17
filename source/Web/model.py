# Import the library
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier
# Read data
data = pd.read_csv("../../data/data_clean.csv")
# Filter Feature
data = data.loc[:,['ph','Hardness','Solids','Chloramines','Sulfate','Conductivity','Organic_carbon','Trihalomethanes','Turbidity','Potability']]
# Setup the data for classifier
x = data.loc[:,['ph','Hardness','Solids','Chloramines','Sulfate','Conductivity','Organic_carbon','Trihalomethanes','Turbidity']]
y = data.loc[:,['Potability']]
oversample = SMOTE()
x_res, y_res = oversample.fit_resample(x, y)
# split data set
x_train, x_test, y_train, y_test = train_test_split(x_res, y_res, test_size=0.3)
model_XGB = XGBClassifier(n_estimators = 1000,learning_rate = 0.0001,max_depth = 15 , subsample = 0.5,random_state=42,min_child_weight=0.5,gamma=0.01,scale_pos_weight=1)
model_XGB.fit(x_train, y_train)
def predict(x):
    predicted_y_XGB = model_XGB.predict(x)
    return predicted_y_XGB
# xx = x_test.head(1)
# predicted_y_XGB = model_XGB.predict(xx)