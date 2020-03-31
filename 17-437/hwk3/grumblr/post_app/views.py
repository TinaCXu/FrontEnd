from django.shortcuts import render
from post_app import forms
from .models import UserProfileInfo,User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
# Create your views here.

def HomeView(request):
    return render(request,'home.html')

#GET request: user want a html
#POST  request: user want to send data to server

def RegisterView(request):

    if request.method == "GET":
        register_form = forms.RegisterForm()
        #isolate the dictionary-context from function render, incase there are lots of key and value
        context = {}
        context['register_form'] = register_form
        return render(request,'registration.html',context)
        
    #if we are here, the request must be post
    if request.method == 'POST':
    #if it is post, user is submitting info by form.
        #step 1 get the form
        register_form = forms.RegisterForm(data=request.POST)
        #step 2 see if it is valid
        if register_form.is_valid():
            #it is valid, store it into the database
            user = User()
            user.username = register_form.cleaned_data['username']
            user.first_name = register_form.cleaned_data['first_name']
            user.last_name = register_form.cleaned_data['last_name']
            user.password = register_form.cleaned_data['password']
            user.email = register_form.cleaned_data['email']
            user.set_password(user.password) #hashing the password

            user_profile = UserProfileInfo()
            user_profile.introduction = register_form.cleaned_data['introduction']

            user.save()
            return HttpResponse("register success")
        #step 3 if it is not valid, return information
        else:
            context = {}
            context['register_form'] = register_form
            return render(request,'registration.html',context)
    return HttpResponse("404")

def LoginView(request):
    if request.method == "GET":
        login_form = forms.LoginForm()
        #isolate the dictionary-context from function render, incase there are lots of key and value
        context = {}
        context['login_form'] = login_form
        return render(request,'login.html',context)

    if request.method == 'POST':
    #if it is post, user is submitting info by form.
        #step 1 get the form
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        #step 2 see if it is valid
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return HttpResponseRedirect(reverse('home'))
            # success page should be linked to personal page, specify it tomorrow
        return render(request,'login.html',context)
    return HttpResponse("404")
