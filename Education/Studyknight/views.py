
import json
from pyexpat.errors import messages
from rest_framework.response import Response
from django.shortcuts import render, HttpResponse
from .forms import InputForm, Nameform
from Studyknight.models import SSC,GD

def index(request):
    context  = {
        'username': "Abhay Panjla ",
        'course' :"Full stack developer "
    }
    return render(request,'hy.html',context)


def index(request):
    context = {}
    context["forms"] = InputForm()
    return render(request, "hy.html", context)


def context(request):
    context = {}
    context["forms"] = InputForm()
    return render(request, "context.html", context)
 

def show(request):
    res = []
    employees = SSC.objects.all()
    for emp in employees:
        data = {"ssc_t": emp.ssc_txt, "em": emp.email}
        res.append(data)
    return HttpResponse(json.dumps(res))


from django.http import HttpResponse


def unow(request):
    tes = []
    students = GD.objects.all()
    
    for stu in students:
        iso_ta = stu.pub_date.isoformat()
        op = {"gd_t": stu.gd_txt, "pub": iso_ta}
        tes.append(op)
    return HttpResponse(json.dumps(tes))
    

from Studyknight.models import Context,Omen

def context(request):   
    if request.method=="POST":
        name=request.POST['name']
        email = request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        print(name,email,content,phone)
        context = Context(name=name,email=email,phone=phone,content=content)
        context.save()
    return render(request, "context.html")


def omen(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        print(name, email, phone)
        omen = Omen(name=name, email=email, phone=phone)
        omen.save()
    return render(request,"omen.html")    


# def context(request):   
#     if request.method=="DELETE":
#         name=request.POST['name']
#         email = request.POST['email']
#         phone=request.POST['phone']
#         content =request.POST['content']
#         print(name,email,content,phone)
#         context = Context(id=1)
#         context.delete()
#     return render(request, "context.html")


# def context(request):   
#     if request.method=="UPDATE":
#         name=request.POST['name']
#         email = request.POST['email']
#         phone=request.POST['phone']
#         content =request.POST['content']
#         print(name,email,content,phone)
#         context = Context(id=1,name=name,email=email,phone=phone,content=content)
#         context.save()
#     return render(request, "context.html")


