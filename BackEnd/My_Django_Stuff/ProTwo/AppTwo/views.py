from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.
def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    my_dict = {'insert me':"Hello I am from AppTwo\help.html!"}
    return render(request,'AppTwo\help.html',context=my_dict)

def users(request):
    webpages_list = User.objects.order_by('first_name')
    first_name_dict = {'user_records':webpages_list}
    return render(request, 'AppTwo\\users.html',context=first_name_dict) 



