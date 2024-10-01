import os
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from flask import Flask, request, flash,render_template,url_for,redirect
from sklearn.preprocessing import MinMaxScaler

from sklearn import metrics
data=pd.read_csv('dataset.txt')
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('ProjectHomepage.html')

@app.route('/soilfertility',methods=['POST'])
def soilfertility():
    
    a0=float(request.form['0'])
    a1=float(request.form['1'])
    a2 =float(request.form['2'])
    a3 =float(request.form['3'])
    a4 =float(request.form['4'])
    a5=float(request.form['5'])
    a6=float(request.form['6'])
    a7 =float(request.form['7'])
    a8 =float(request.form['8'])
    a9 =float(request.form['9'])
    a10=float(request.form['10'])
    a11=float(request.form['11'])
    a12 =float(request.form['12'])
    a13=float(request.form['13'])
    if(a0==0 and a1==0 and a2==0 and a3==0 and a4==0 and a5==0 and a6==0 and a7==0 and a8==0 and a9==0 and a10==0 and a11==0 and a12==0 and a13==0):
        return render_template('ProjectHomepage.html',prediction_text=0)
    X, Y = data[data.columns[1:]], data['Vegetation Cover']
    dict={'NO3':[a0],'NH4':[a1],'P':[a2],'K':[a3],'SO4':[a4],'B':[a5],'Organic Matter':[a6],'pH':[a7],'Zn':[a8],'Cu':[a9],'Fe':[a10],'Ca':[a11],'Mg':[a12],'Na':[a13]}
    df1 = pd.DataFrame(dict)
    df = pd.concat([X, df1], ignore_index = True)
    df.reset_index()
    X=df
    scaler = MinMaxScaler()
    X, Y = scaler.fit_transform(X.values), scaler.fit_transform(Y.values.reshape(-1,1))
    l1=[X[408]]
    X = X[:-1]  

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.10, random_state=43)

    forestRegressor = RandomForestRegressor(criterion='poisson', max_depth=8, n_estimators=10, random_state=0)
    forestRegressor.fit(X_train, Y_train)
    y_pred = forestRegressor .predict(X_test)
    prediction = forestRegressor .predict(l1)
    print(l1)
    text=""
    if(prediction<90):
        if(a0<12.75 or a2<47 or a8<0.6 or a3<15 or a6<0.28 or a10<1):
            text="Your Soil is less fertile.You may try increasing these nutrients "
        if(a0<12.75):
            text=text+"NO3 "
        if(a2<47):
            text=text+"P "
        if(a8<0.6):
            text=text+"Zn "
        if(a3<15):
            text=text+"K "
        if(a6<0.28):
            text=text+"Organic Matter "
        if(a10<1):
            text=text+"Fe "
    if(prediction>=90):
        text="Your soil is high fertile."		
    if(prediction>0 and prediction<1):
        return render_template('Results.html',content=text,prediction_text=np.round(prediction*100).astype(int))
if __name__ == "__main__":
    app.run(debug=True)
