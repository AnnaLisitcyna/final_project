from flask import Flask, request
import joblib
import numpy


MODEL_PATH = 'mlmodels/model.pkl'
MODEL_PATH_1 = 'mlmodels/model1.pkl'

app = Flask(__name__)
model = joblib.load(MODEL_PATH)
model1 = joblib.load(MODEL_PATH_1)
@app.route("/predict_price", methods = ["GET"])

def predict():
    args = request.args
    floor = args.get('floor', type = int)
    open_plan = args.get('open_plan', type = int)
    rooms = args.get('rooms', type = int)
    area = args.get('area', type = float)

    x = numpy.array([floor, open_plan, rooms, area]).reshape(1,-1)
    result = model.predict(x)
    result = result.reshape(1,-1)

    return str(result[0][0])

def predict1():
    args = request.args
    floor = args.get('floor', type = int)
    open_plan = args.get('open_plan', type = int)
    rooms = args.get('rooms', type = int)
    area = args.get('area', type = float)
    agent_fee = args.get('agent_fee', type = float)
    renovation = args.get('renovation', type = float)

    x1 = numpy.array([floor, open_plan, rooms, area, agent_fee, renovation]).reshape(1,-1)
    result1 = model1.predict1(x)
    result1 = result1.reshape(1,-1)

    return str(result1[0][0])

if __name__ == '__main__':
    app.run(debug = True, port = 5444, host = '0.0.0.0')
