from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm 


# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            #grab things in user_form
            user = user_form.save()
            user.set_password(user.password) #hashing the password
            user.save() #save the hashed password to the database

            #grab things in profile_form
            profile = profile_form.save(commit=False)
            #do not save yet, may get error when overwrite user when saving profile
            profile.user = user
            # proile.user = profile_form.user = UserProfileInfoForm.user = UserProfileInfo.user(inherite)
            # user = user_form =UserForm
            # this equation stands for the one to one relationship in models

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic'] #dictionary of the files user uploaded in request

            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'basic_app/registration.html',
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered})    