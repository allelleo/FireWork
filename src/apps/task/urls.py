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
from .views import CreateTaskAPIView, ReadTaskAPIView, CreateTaskAnswer,GetCurrentUserTasks,GetMyCreatedTasks, GetTasks

urlpatterns = [
    path('create/', CreateTaskAPIView.as_view()),
    path('read/', ReadTaskAPIView.as_view()),
    path('answer/', CreateTaskAnswer.as_view()),
    path('my/', GetCurrentUserTasks.as_view()),
    path('myCreated/', GetMyCreatedTasks.as_view()),
    path('All/', GetTasks.as_view()),

]
