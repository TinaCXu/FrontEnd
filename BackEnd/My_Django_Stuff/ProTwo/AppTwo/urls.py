from django.urls import path
from django.conf.urls import url
from AppTwo import views

urlpatterns = [
    path('',views.help, name = 'help'),
]