import json, csv
import numpy as np, pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split

def predictionTill2100(countryStr, cropStr):
    dfc = pd.read_csv("data/{a}_crop.csv".format(a=countryStr))
    dfc.columns = ['Entity', 'Code', 'Year', 'Temp', 'Wheat', 'Rice', 'Bananas', 'Maize', 'Soybeans', 'Potatoes', 'Beans', 'Peas', 'Cassava', 'Cocoa', 'Barley']
    X = dfc[['Year', 'Temp']]
    y = dfc[cropStr]
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.1, shuffle=False)
    lr = linear_model.LinearRegression()
    lr.fit(x_train.values, y_train)

    dfc2 = pd.read_csv("data/{a}_temp.csv".format(a=countryStr))
    dfc2.columns = ['Year', 'Temp']
    print(dfc2)
    future_data = {}
    future_data['Year'] = dfc2['Year'].values
    future_data['Predicted'] = lr.predict(dfc2.values) 
    print(future_data)
    
    # Plotting
    plt.figure(figsize=(10, 8))
    plt.scatter(x_train['Year'], y_train, color='blue', label='Training Data')
    plt.scatter(x_test['Year'], y_test, color='green', label='Testing Data')
    plt.plot(x_train['Year'], lr.predict(x_train), color='red', linewidth=2, label='Linear Regression')
    plt.plot(future_data['Year'], future_data['Predicted'], color='orange', linestyle='--', label='Predicted Data')
    plt.xlabel('Year')
    plt.ylabel(cropStr)
    plt.title('Training, Testing, and Predicted Data')
    plt.legend()
    plt.grid(True)
    sns.despine()
    plt.show()

def showTestingTraining(countryStr, cropStr):
    dfc = pd.read_csv("data/{a}_crop.csv".format(a=countryStr))
    dfc.columns = ['Entity', 'Code', 'Year', 'Temp', 'Wheat', 'Rice', 'Bananas', 'Maize', 'Soybeans', 'Potatoes', 'Beans', 'Peas', 'Cassava', 'Cocoa', 'Barley']
    X = dfc[['Year', 'Temp']]
    y = dfc[cropStr]
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.1, shuffle=False)
    lr = linear_model.LinearRegression()
    lr.fit(x_train.values, y_train)

    plt.figure(figsize=(10, 6))
    plt.scatter(x_train['Year'], y_train, color='blue', label='Training Data')
    plt.scatter(x_test['Year'], y_test, color='green', label='Testing Data')
    plt.plot(x_train['Year'], lr.predict(x_train), color='red', linewidth=2, label='Linear Regression')
    plt.xlabel('Year')
    plt.ylabel(cropStr)
    plt.title('Training and Testing Model')
    plt.legend()
    plt.grid(True)
    sns.despine()
    plt.show()

showTestingTraining('China', 'Wheat')
predictionTill2100('China', 'Wheat')