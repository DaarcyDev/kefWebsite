from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')
    
def about(request):
    return render(request, 'about.html')

def signin(request):
    return render(request, 'signIn.html')

def signup(request):
    return render(request, 'signUp.html')