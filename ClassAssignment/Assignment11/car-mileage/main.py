import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from sklearn import preprocessing
import pickle

app = Flask(__name__)
model = pickle.load(open('', 'rb'))
cols=[]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    feature_list = request.form.to_dict()
    feature_list = list(feature_list.values())
    feature_list = list(map(int, feature_list))
    final_features = np.array(feature_list).reshape() 
    
    prediction = model.predict(final_features)
    output = int(prediction[0])

    return render_template('index.html', prediction_text='${}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)