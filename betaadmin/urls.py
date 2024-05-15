from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='beta'),
    path('inbox/',inbox,name='inbox'),
    path('dashboard/',dashboard,name='dashboard'),
    path('admin/', admindashboard, name='admin'),
    path('logout/',logout,name='logout'),
    path('login/',login,name='login'),
    path('signup/',register,name='signup'),
    path('editProfile/',editprofile,name='editprofile'),
    path('viewprofile/<str:id>/',viewProfile,name='viewprofile'),
    path('forgot-password/',forget,name='forgot'),
    path('forgot-password/<token>/',forgotreset,name='reset')
]