from django.shortcuts import render, get_object_or_404
from post_app import forms
from .models import UserProfileInfo,User,UserPost
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms.boundfield import BoundField

from datetime import datetime
from datetime import timedelta

import json

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

            # u = User.objects.get(username=user.username)
            # user_profile.introduction

            user.save()

            user_profile = UserProfileInfo()
            user_profile.introduction = register_form.cleaned_data['introduction']
            user_profile.age = register_form.cleaned_data['age']
            user_profile.user = user
            user_profile.save()
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
            return HttpResponseRedirect(reverse('global'))
            # success page should be linked to personal page, specify it tomorrow
        return render(request,'login.html',context)
    return HttpResponse("404")

@login_required
def logoutView(request):
    logout(request)
    return render(request,'home.html')

@login_required
def PostView(request):
    if request.method == 'GET':
        post_form = forms.PostForm
        post_list = UserPost.objects.order_by('-post_time')
        context = {}
        context['post_form'] = post_form
        context['post_records'] = post_list
        return render(request,'global_stream.html',context)
    if request.method == 'POST':
        #if it is post, user is submitting info by form.
        #step 1 get the form
        #3 fields, post is provided by request.POST
        # user and time is provided by instance post, use instance to add it to post_form
        post = UserPost(user=request.user)
        post_form = forms.PostForm(data=request.POST, instance=post)

        # updatepost = UpdatePost()
        # updatepost = request.POST['latest_post_time']
        # updatepost.save()

        #step 2 see if it is valid
        if post_form.is_valid():
            #it is valid, store it into the database
            post_form.save()            
            return HttpResponse("Post success")
        #step 3 if it is not valid, return information
        else:
            context = {}
            context['post_form'] = post_form
            return render(request,'global_stream.html',context)
    return HttpResponse("404")


def UpdatePostView(request, timestamp):
    print('UpdatePostView:', timestamp)
    if request.method == 'GET':
        #1. get posts newer than timestamp
        # TODO: order?:ok
        # TODO: gte? gt = great, gte = great or equal.
        # TODO: max time is a string of time. check if string is time.
        existing_posts = UserPost.objects.order_by('-post_time')
        print(str(existing_posts[0].post_time))
        print(type(existing_posts[0].post_time))

        print(timestamp)
        print(type(timestamp))

        if str(existing_posts[0].post_time) == timestamp:
            newest_posts={
                "timestamp": timestamp,
                "posts": "" 
            }
            return HttpResponse(json.dumps(newest_posts), content_type='application/json')
        else:
            newest_posts = UserPost.objects.filter(post_time__gt=timestamp).order_by('-post_time')
            # print(newest_post)
            print(len(newest_posts))
            print(newest_posts)
            print(newest_posts[0].user)
            print(newest_posts[0].post)
            print(newest_posts[0].post_time)
            print(newest_posts[0].user.id)

            newest_post_pool = []
            for i in range(len(newest_posts)):
                newest_post = {
                    "timestamp":(newest_posts[i].post_time+timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S'),
                    "user":newest_posts[i].user.username,
                    "post":newest_posts[i].post,
                    "user_id":str(newest_posts[i].user.id),
                    }
                newest_post_pool.append(newest_post)
            print(newest_post_pool)

            #2. return them and newest timestamp (json format)
            # TODO:last post is the newest post?
            newest_posts={
                "timestamp": str(newest_posts[0].post_time),
                "posts":  newest_post_pool
            }
            return HttpResponse(json.dumps(newest_posts), content_type='application/json')
    return HttpResponse("404")

@login_required
def PersonalView(request,userID):
    print('UpdatePersonalView:', userID)
    if request.method == 'GET':
        target_user = User.objects.get(id=userID)
        target_user_first_name = target_user.first_name
        target_user_last_name =target_user.last_name

        post_form = forms.PostForm
        post_list = UserPost.objects.filter(user=target_user).order_by('-post_time')
        introduction = get_object_or_404(UserProfileInfo,user=target_user).introduction       
        print(introduction)
        print(request.user.id)

        context = {}
        context['post_form'] = post_form
        context['post_records'] = post_list
        context['user_name'] = post_list[0].user
        context['user_introduction'] = introduction
        context['first_name'] = target_user_first_name
        context['last_name'] = target_user_last_name
        return render(request,'personal.html',context)

    if request.method == 'POST':
        #if it is post, user is submitting info by form.
        #step 1 get the form
        #3 fields, post is provided by request.POST
        # user and time is provided by instance post, use instance to add it to post_form
        post = UserPost(user=request.user)
        post_form = forms.PostForm(data=request.POST, instance=post)

        # updatepost = UpdatePost()
        # updatepost = request.POST['latest_post_time']
        # updatepost.save()

        #step 2 see if it is valid
        if post_form.is_valid():
            #it is valid, store it into the database
            post_form.save()            
            return HttpResponse("Post success")
        #step 3 if it is not valid, return information
        else:
            context = {}
            context['post_form'] = post_form
            return render(request,'global_stream.html',context)
    return HttpResponse("404")

def UpdatePersonalView(request, target_user, timestamp):
    print('UpdatePostView:', timestamp)
    if request.method == 'GET':
        existing_posts = UserPost.objects.filter(user=target_user).order_by('-post_time')
        print(str(existing_posts[0].post_time))
        print(type(existing_posts[0].post_time))

        print(timestamp)
        print(type(timestamp))

        if str(existing_posts[0].post_time) == timestamp:
            newest_posts={
                "timestamp": timestamp,
                "posts": "" 
            }
            return HttpResponse(json.dumps(newest_posts), content_type='application/json')
        else:
            newest_posts = UserPost.objects.filter(user=target_user,post_time__gt=timestamp).order_by('-post_time')
            # print(newest_post)
            print(len(newest_posts))
            print(newest_posts)
            print(newest_posts[0].user)
            print(newest_posts[0].post)
            print(newest_posts[0].post_time)
            print(newest_posts[0].user.id)

            newest_post_pool = []
            for i in range(len(newest_posts)):
                newest_post = {
                    "timestamp":(newest_posts[i].post_time+timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S'),
                    # "user":newest_posts[i].user.username,
                    "post":newest_posts[i].post,
                    # "user_id":str(newest_posts[i].user.id),
                    }
                newest_post_pool.append(newest_post)
            print(newest_post_pool)

            #2. return them and newest timestamp (json format)
            # TODO:last post is the newest post?
            newest_posts={
                "timestamp": str(newest_posts[0].post_time),
                "posts":  newest_post_pool
            }
            return HttpResponse(json.dumps(newest_posts), content_type='application/json')
    return HttpResponse("404")

@login_required
def PersonalProfileView(request):
    if request.method == 'GET':
        personal_profile = UserProfileInfo.objects.get(user=request.user)
        print(personal_profile)
        print(personal_profile.introduction)
        print(personal_profile.age)

        context = {}
        context['first_name'] = request.user.first_name
        context['last_name'] = request.user.last_name
        context['age'] = personal_profile.age
        context['introduction'] = personal_profile.introduction
        context['password'] = request.user.password

        return render(request,'personal_profile.html',context)
    if request.method == 'POST':
        return render(request,'personal_update.html')

@login_required
# static part for personal profile
def PersonalProfileFormView(request):
    if request.method == 'GET':
        # prepate the form skelton for html
        profile_form = forms.PersonalProfileForm()
        password_form = forms.PersonalPasswordForm()
        context = {}
        context['profile_form'] = profile_form
        context['password_form'] = password_form
        context['user_id'] = request.user.id

    return render(request,'personal_update.html',context)

@login_required
# dynamic part for personal profile
def PersonalProfileUpdateView(request, userID):
    if request.method == 'GET':
        # prepare the initial form data for user
        personal_profile = UserProfileInfo.objects.get(user=request.user)
        personal_data = {
            "username":request.user.username,
            "first_name":request.user.first_name,
            "last_name":request.user.last_name,
            "email":request.user.email,
            "age":personal_profile.age,
            "introduction":personal_profile.introduction,
        }
        print(personal_data)
        # return the data to frontend
        return HttpResponse(json.dumps(personal_data), content_type='application/json')



