from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('createUser',views.createUser,name='createUser'),
    path('signup',views.signup,name='signup'),
    path('checkUser',views.checkUser,name='checkUser'),
    path('userDetails/<int:id>',views.userDetails,name='userDetails')
]
