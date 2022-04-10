from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
   return render(request, 'index.html')

def blog(request):
       
   return render(request, 'blog.html')