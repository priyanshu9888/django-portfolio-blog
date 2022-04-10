from django.contrib import admin
from django.urls import path
from home import views
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
        path("", views.index, name='home'),
        path("blog/", views.blog, name='blog'),

]
