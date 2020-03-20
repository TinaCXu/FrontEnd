from django.shortcuts import render #in order to use dictionary
from django.http import HttpResponse #from django module import django object
from first_app.models import Topic,Webpage,AccessRecord #import models

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
        #use template tagging to inject template to HTML
    return render(request, 'first_app\index.html',context=date_dict) 
        #use render to grab stuff from model itself(aka.AccessRecord)
    # my_dict = {'insert_me':"Hello I am from first_app\index.html!"}
    # return render(request, 'first_app\index.html',context=my_dict)

#we should map this view to urls.py
