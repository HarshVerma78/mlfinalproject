import numpy as np 
import pandas as pd
from flask import Flask,request,jsonify,render_template

import joblib
server=Flask(__name__)
model=joblib.load("netflix.pkl")
@server.route('/')
def home():
    print(model)
    return render_template('index.html')

@server.route('/predict',methods=['POST'])
def predict():
    movie = request.form.values()
    frecommend = model.predict()
    umovies = frecommend(movie)

    return render_template('index.html', prediction_text='Predicted movies  {}'.format(result_movies))

# @server.route('/predict_api',methods=['POST'])
# def predict_api():
#     '''
#     For direct API calls trought request
#     '''
#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])
#     output = prediction[0]
#     return jsonify(output)

if __name__ == "__main__":
    server.run(debug=True)

    