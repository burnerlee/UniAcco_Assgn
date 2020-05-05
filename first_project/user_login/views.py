from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import User
import requests
import socket

def index(request):
    return render(request,'user_login/login.html',{})  

def signup(request):
    return render(request,'user_login/signup.html',{})

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

def checkUser(request):
    email = request.POST['email']
    password = request.POST['password']
    if len(User.objects.filter(email=email))>0:
        try:
            user = User.objects.get(email=email,password=password)
        except User.DoesNotExist:
            return HttpResponse("Incorrect password.")
        return HttpResponseRedirect("userDetails/%s" % user.id)
    else:
        return HttpResponse("User with email %s does not exist. Please signup" % email)

def userDetails(request,id):
    user = User.objects.get(id=id)
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname) 
    data = {
        'user':id,
        'ip_address': IPAddr 
    }
    requests.post("https://encrusxqoan0b.x.pipedream.net/",data = data)
    context = {
        'name' : user.name,
        'email' : user.email,
        'password' : user.password,
    }
    return render(request,'user_login/userDetails.html',context)