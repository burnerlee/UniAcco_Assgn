from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import User
import requests
import socket

def index(request):
    return render(request,'user_login/login.html',{})                   #renders the login page.

def signup(request):
    return render(request,'user_login/signup.html',{})                  #renders the signup page.

#createUser uses the POST data to create a new user and saves it in the database.
#Checks if the user with same email already exists.
#Redirect to login page after successful signup.
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

#checkUser validates the Credentials of the user, authorizes access by session variable.
def checkUser(request):
    email = request.POST['email']
    password = request.POST['password']
    if len(User.objects.filter(email=email))>0:
        try:
            user = User.objects.get(email=email,password=password)
        except User.DoesNotExist:
            return HttpResponse("Incorrect password.")
        authenticate = "auth_user_" + str(user.id)
        request.session[authenticate] = True
        return HttpResponseRedirect("userDetails/%s" % user.id)
    else:
        return HttpResponse("User with email %s does not exist. Please signup" % email)

#userDetails displays the details of the user requested.
#it sends a webhook to the specified address.
def userDetails(request,id):
    authenticate = "auth_user_" + str(id)
    try:
        is_authorized = request.session[authenticate]
        if not is_authorized:
            return HttpResponse("You are not authorized to access this resource")
    except:
        return HttpResponse("You are not authorized to access this resource")
    user = User.objects.get(id=id)
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)                                 #IP Address of the server.
    data = {
        'user':id,
        'ip_address': IPAddr 
    }
    requests.post("https://encrusxqoan0b.x.pipedream.net/",data = data)     #Webook sent.
    context = {
        'name' : user.name,
        'email' : user.email,
        'password' : user.password,
    }
    return render(request,'user_login/userDetails.html',context)