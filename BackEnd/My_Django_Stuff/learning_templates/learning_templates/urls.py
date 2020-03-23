"""learning_templates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from basic_app import views
from django.urls import include,path

urlpatterns = [
    path('',views.index, name='index'), #''=domain page,home page
    path('admin/', admin.site.urls),
    path('basic_app/',include('basic_app.urls')) 
    #there is no page /basic_app/, but /basic_app/other(url name in basic_app.urls)
]
