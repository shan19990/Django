from django.shortcuts import render
from prediction.forms import Predict
import joblib
import numpy as np
import pandas as pd
# Create your views here.

def prediction(request):

    loaded_model = joblib.load(r'C:\Users\Admin\Desktop\My_Django_Stuff\salary\MachineLearning\salaryPrediction.pkl')
    
    strpred = None

    if request.method == 'POST':
        form = Predict(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            yoe = form.cleaned_data['yoe']
            education = form.cleaned_data['education']

            if education == "bachelor":
                master = 0
                phd = 0
            elif education == "masters":
                master = 1
                phd = 0
            elif education == "phd":
                master = 0
                phd = 1
            data = np.array([age,yoe,master,phd])
            data_reshaped = data.reshape(1, -1)
            pred = loaded_model.predict(data_reshaped)
            strpred = np.array_str(pred)[1:-1]
            print("predicted value:", strpred)
    else:
        form = Predict()
    return render(request,"prediction/prediction.html",{"form":form,"pred":strpred})
            

    
