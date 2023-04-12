from flask import *
import json, csv
import numpy as np, pandas as pd
# use scikit-learn
from sklearn import linear_model
from sklearn.model_selection import train_test_split
app = Flask(__name__)

print("server started")

@app.route('/', methods=['GET'])
def home():
    message = {'status' : 200, 'message' : 'Running'}
    json_dump = json.dumps(message)
    response = make_response(json_dump)
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/v', methods=['GET'])
def version():
    message = {'version' : '1.1.1', 'desc' : 'prediction check'}
    json_dump = json.dumps(message)
    response = make_response(json_dump)
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/py', methods=['GET'])
def py():
    countryStr = str(request.args.get('country')).lower()
    cropStr = request.args.get('crop')
    yearPredStart = int(request.args.get('start'))
    yearPredEnd = int(request.args.get('end')) + 1
    temperatureMap = {}
    with open("{a}_temp.csv".format(a=countryStr), 'r') as f:
        for line in csv.reader(f):
            temperatureMap[line[0]] = line[1]
    predictedTempList = []
    resTemp = []
    for yearPred in range(yearPredStart, yearPredEnd):
        predictedTempList.append([yearPred, float(temperatureMap[str(yearPred)])])
        resTemp.append(float(temperatureMap[str(yearPred)]))
    
    dfc = pd.read_csv("{a}_crop.csv".format(a=countryStr))
    dfc.columns = ['Entity','Code','Year','Temp','Wheat','Rice','Bananas','Maize','Soybeans','Potatoes','Beans','Peas','Cassava','Cocoa','Barley']
    # lr = lrBasic(dfc, cropStr)
    X = dfc[['Year', 'Temp']]
    y = dfc[cropStr]
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.1, shuffle=False)
    lr = linear_model.LinearRegression()
    lr.fit(x_train.values, y_train)
    resProd = lr.predict(predictedTempList)
    message = {
        'country' : countryStr, 
        'crop' : cropStr, 
        'start' : yearPredStart, 
        'end' : yearPredEnd - 1, 
        'temperature' : resTemp,
        'production' : resProd.tolist()
        }
    json_dump = json.dumps(message)
    response = make_response(json_dump)
    response.headers['Content-Type'] = 'application/json'
    return response

if __name__ == '__main__':
    print("server running")
    app.run()
    # app.run(port=3000)