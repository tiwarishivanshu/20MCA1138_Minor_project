from django.shortcuts import render
from django.http import HttpResponse as res
import math 
import pandas as pd
import pickle as p
model=p.load(open('/home/shivanshu/Documents/car/django/web/web/car.pkl','rb+'))
def index(request):
    return render(request,"index.html")
def predict(request):
    if request.method=='POST':
        temp={}
        temp['location']=request.POST.get('location')
        temp['year']=request.POST.get('year')
        temp['Kl']=request.POST.get('Kl')
        temp['fule_type']=request.POST.get('fule_type')
        temp['transmission']=request.POST.get('transmission')
        temp['owner']=request.POST.get('owner')
        temp['Mileage']=request.POST.get('Mileage')
        temp['Engine']=request.POST.get('Engine')
        temp['Power']=request.POST.get('Power')
        temp['Seats']=request.POST.get('Seats')
        temp['New_Price']=request.POST.get('New_Price')
        test=[]
        for i,j in temp.items():
            print(j)
            test.append(j)
        test=[test]
        score=model.predict(test)
        score=score[0]
        context={'result':score}
        return render(request, 'result.html',context)
