from django.shortcuts import render #in order to use dictionary
from django.http import HttpResponse #from django module import django object

# Create your views here.

def index(request):
    my_dict = {'insert_me':"Hello I am from first_app\index.html!"}
    return render(request, 'first_app\index.html',context=my_dict)

#we should map this view to urls.py
