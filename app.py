import numpy as np 
import pandas as pd
from flask import Flask,request,jsonify,render_template
import joblib
app=Flask(__name__)
model=joblib.load("netflix.pkl")
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict(movie):
    '''
    For rendering results on HTML GUI
    '''
    movie = request.form.values()
    result = model.predict(movie)
    # for i in movies_list:
    #     result_movies += new_movies.iloc[i[0]].title
    return render_template('index.html', prediction_text='Predicted movies  {}'.format(result))

# @app.route('/predict_api',methods=['POST'])
# def predict_api():
#     '''
#     For direct API calls trought request
#     '''
#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])
#     output = prediction[0]
#     return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)