from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo import forms


# Create your views here.
def index(request):
    return HttpResponse("Go to /signin to sign up!")

def help(request):
    my_dict = {'insert me':"Hello I am from AppTwo\help.html!"}
    return render(request,'AppTwo\help.html',context=my_dict)

def users(request):
    webpages_list = User.objects.order_by('first_name')
    first_name_dict = {'user_records':webpages_list}
    return render(request, 'AppTwo\\users.html',context=first_name_dict) 

def form_name_view(request):
    form = forms.FormName

    # grab the data post by user
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        #this is an instance,(request.POST) is a complex attribute package
        if form.is_valid():
            #DO SOMETHING CODE
            form.save(commit=True)#save the form into database
            return index(request)#take it back to home page
        else:
            print("ERROR FOR INVALID")
    return render(request,'AppTwo/form_page.html',{'form':form})


