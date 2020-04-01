from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
from . import models

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!' 
        return context

class SchoolListView(ListView):
    model = models.School
    # for ListView, it will automatically create a context dictionary 'school_list', which could be injected in HTML
    context_object_name = 'schools'
    # we could create our own context dictionary

class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'basic_app/school_detail.html'
    # for DetailView, it will automatically create a context dictionary 'school', which could be injected in HTML
    context_object_name = 'school_detail'