"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import EndpointView, GetCurrentUserData,ChangeUserPhoto, AddSkill,AllSkills, GetCustomers, GetWorkers,GetUserById,CreateNorify

urlpatterns = [
    path('endpoint/', EndpointView.as_view()),
    path('data/', GetCurrentUserData.as_view()),
    path('changePhoto/', ChangeUserPhoto.as_view()),
    path('skill/addSkill/', AddSkill.as_view()),
    path('skill/all/', AllSkills.as_view()),
    path('GetWorkers/', GetWorkers.as_view()),
    path('GetCustomers/', GetCustomers.as_view()),
    path('get_user/', GetUserById.as_view()),
    path('newNotify/', CreateNorify.as_view()),
]
