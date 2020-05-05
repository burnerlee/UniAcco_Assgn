from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import User
# Create your views here.
def index(request):
    context = {}
    return render(request,'user_login/signup.html',context)  


def createUser(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    if len(User.objects.filter(email=email))>0:
        return HttpResponse("User with email %s already exists" % email)
    else:    
        newUser = User(name=name,email=email,password=password)
        newUser.save()
        return HttpResponseRedirect('/user_login') 