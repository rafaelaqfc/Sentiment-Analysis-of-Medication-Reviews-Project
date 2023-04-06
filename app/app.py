from flask import render_template, request, jsonify,Flask
import flask
import numpy as np
import traceback # Allows you to send error to user
import pickle
import pandas as pd

# App definition
app = Flask(__name__)


#=========================================================================================
# Importing models
with open('ensemble_model.pkl', 'rb') as f:
   model = pickle.load(f)

rating_map = {0: 'Negative', 1: 'Neutral', 2: 'Positive'}
#=========================================================================================


@app.route('/')
def welcome():
   return "Welcome to Rafaela's medication review app -- go to /predict to try it!"


@app.route('/predict', methods=['POST','GET'])
def predict_review():
   if flask.request.method == 'GET':
      return "This is the GET page... you need to POST here (try some Python code or use Postman)"
   
   if flask.request.method == 'POST':
      data = request.json

      #=========================================================================================
      X = data['review']
      y = model.predict(X)
      ratings = [rating_map[k] for k in y]
      #=========================================================================================

      return jsonify({
         "ratings": ratings
      })
   
if __name__ == "__main__":
   app.run()
