from flask import Flask, request
import joblib
import numpy


MODEL_PATH = 'mlmodels/model.pkl'
MODEL_PATH_1 = 'mlmodels/model1.pkl'

app = Flask(__name__)
@app.route("/predict_price", methods = ["GET"])

def predict():
    args = request.args
    floor = args.get('floor', type = int)
    open_plan = args.get('open_plan', type = int)
    rooms = args.get('rooms', type = int)
    area = args.get('area', type = float)
    agent_fee = args.get('agent_fee', type = float)
    renovation = args.get('renovation', type = float)

    model = args.get('model_v', type = int)

    if model == 1:
        model = joblib.load(MODEL_PATH)
        x = numpy.array([floor, open_plan, rooms, area]).reshape(1, -1)
        result = model.predict(x)
        result = result.reshape(1, -1)

        return str(result[0][0])
    
    if model == 2:
        model = joblib.load(MODEL_PATH_1)
        x = numpy.array([floor, open_plan, rooms, area, agent_fee, renovation]).reshape(1, -1)
        result = model.predict(x)
        result = result.reshape(1, -1)

        return str(result[0][0])

if __name__ == '__main__':
    app.run(debug = True, port = 5444, host = '0.0.0.0')
