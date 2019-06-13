from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('backlog/', views.getbacklog, name='backlog'),
    path('storydetails/<int:id>', views.getstorydetails, name='storydetails'),
    path('newstory/', views.newstory, name='newstory'),
    path('newtask/', views.newtask, name='newtask'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]