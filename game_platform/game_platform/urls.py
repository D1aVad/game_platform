"""
URL configuration for game_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path 
from task4.views import main
from task4.views import sail
from task4.views import contacts
from task5.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('sail/', sail),
    path('contacts/', contacts),
    path('register/', index),
]
