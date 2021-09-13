from django.http import HttpResponse
from django.shortcuts import render
import joblib


def home(request):
    return render(request,"home.html")

def result(request):
    cls =joblib.load("finallized model")

    

    lis = []

    lis.append(request.POST.get("id"))
    lis.append(request.POST.get("income"))
    lis.append(request.POST.get("age"))
    lis.append(request.POST.get("experience"))
    lis.append(request.POST.get("married/single"))
    lis.append(request.POST.get("house_ownership"))
    lis.append(request.POST.get("car_ownership"))
    lis.append(request.POST.get("profession"))
    lis.append(request.POST.get("CITY"))
    lis.append(request.POST.get("state"))
    lis.append(request.POST.get("CURRENT_JOB_YRS"))
    lis.append(request.POST.get("CURRENT_HOUSE_YRS"))

    # res= request.POST.get("id")
    # return HttpResponse(lis)


    ans=cls.predict([lis])
    return render(request,'result.html',{'ans':ans})

    










    