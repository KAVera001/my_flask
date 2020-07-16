

from app import app
from flask import render_template, url_for, flash, get_flashed_messages, redirect, request
from datetime import datetime

import forms
from sql_alc import *


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/info', methods=['GET', 'POST'])
def info():
    form = forms.EnterIdInfo()
    flash('Enter parameter = 1 if you want to see actual values, 2 - if you want to see in percent')
    if form.validate_on_submit():
        try: 
           id = form.title.data
           par = form.title_p.data
           res = find_data(id,par)
           return render_template('answer_info.html', session = id, resultA = res[1],
                               resultB = res[2], resultC = res[3], resultD = res[4])
          
          
        except: 
            flash('Session_id was not found')
            render_template('info.html', form=form)
           
    return render_template('info.html', form=form)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    form = forms.EnterIdPredict()
    if form.validate_on_submit():
        try: 
           id = form.title.data
           ex = data_for_gender_prediction(id)
           res = predict_function(ex)
           return render_template('answer_predict.html', session=id, result = res)
           
            
        except: 
            flash('Session_id was not found')
            render_template('predict.html', form=form)
        
            
    return render_template('predict.html', form=form)



