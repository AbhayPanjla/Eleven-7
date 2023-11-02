from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name="index"),
    path('context/',views.context,name="context"),
    path('omen/',views.omen,name="omen"),
    path('show',views.show,name= "show"),
    path('unow',views.unow,name= "unow"),

]