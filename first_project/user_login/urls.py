from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),                                  #Login page.
    path('createUser',views.createUser,name='createUser'),              #userCreate Page.
    path('signup',views.signup,name='signup'),                          #Signup page.
    path('checkUser',views.checkUser,name='checkUser'),                 #checkUser Credentials page.
    path('userDetails/<int:id>',views.userDetails,name='userDetails')   #display userDetails page.
]
