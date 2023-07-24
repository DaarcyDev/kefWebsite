from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import productForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')
    
def about(request):
    return render(request, 'about.html')

def signin(request):
    if(request.method == 'GET'):
        return render (request, "signIn.html")
    else:
        user = authenticate(request, username = request.POST["username"],password = request.POST["password"])
        if(user is None):
            return render(request, "signIn.html",{
                "error": "user or password is incorrect"
            })
        else:
            login(request, user)
            return redirect("index") 

def signup(request):

    if request.method == 'GET':
        return render(request, 'signUp.html')
    else:
        print(request.POST)
        if(request.POST["password1"] == request.POST["password2"]):
            #register user
            try:
                user = User.objects.create_user(username = request.POST["username"],password = request.POST["password1"])
                user.save()
                return  redirect("index")
            except:
                return render(request, 'signUp.html',{
                    "error": "User already exist"
                })

        else:
            return render(request, 'signUp.html',{
                "error": "password dont match"
            })

def createProduct(request):
    if(request.method == "GET"):
        return render(request, 'createProduct.html',{
            'form': productForm
        })
    else:
        try:
            form = productForm(request.POST, request.FILES)  # Agrega request.FILES para manejar la carga de archivos
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            return redirect("admin")
        except:
            return render(request, 'createProduct.html',{
            'form': productForm,
            'error': 'please provide valide data'
        })

def signout (request):
    logout(request)
    return redirect("index")

def product(request):
    return render(request, 'product.html')

def adminProduct(request):
    return render(request, 'adminProduct.html')

def indexAdmin(request):
    return render(request, 'admin.html')

