from django.shortcuts import render
from post_app import forms

# Create your views here.

def HomeView(request):
    return render(request,'home.html')

def RegisterView(request):
    user_form = forms.UserForm()
    
    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        if user_form.is_valid():
            return HttpResponse("注册成功")

    return render(request,'registration.html',{'user_form':user_form})
