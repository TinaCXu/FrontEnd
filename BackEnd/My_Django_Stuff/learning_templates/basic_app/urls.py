from django.conf.urls import url
from basic_app import views

#TEMPLATE TAGGING
app_name = 'basic_app'
#django will look for basic_app and find urls that matches  
#this name should match the tag in relative_url_templates

urlpatterns = [
    url('relative/',views.relative,name='relative'), #domain name/basic_app/relative
    url('other/',views.other,name='other'), #domain name/basic_app/other
]