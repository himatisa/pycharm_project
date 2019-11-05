import numpy as np
from flask import Flask, abort, jsonify, request
import pickle

#regressor = pickle.load(open('C:/Users/kyriakos.bilias/TeamBigD-2/forest100_regression.pkl', 'rb'))
my_knn=pickle.load(open('iris_knn.pkl','rb'))
app = Flask(__name__)


@app.route("/api", methods=['POST'])
def make_predict():
    data = request.get_json(force=True)
    predict_request = [data['sl'], data['sw'], data['pl'],data['pw']]
    predict_request = np.array(predict_request)


    y_hat = my_knn.predict([predict_request])
    output = [y_hat[0]]
    return jsonify(results=output)


if __name__ == '__main__':
    app.run(port=9000, debug=True)