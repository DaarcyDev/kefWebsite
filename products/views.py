from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import productForm
from .models import Product
from django.contrib.auth.decorators import user_passes_test, login_required

# Create your views here.
def user_is_specific_user(user):
    return user.username == 'daarcydev'  # Cambia 'nombre_de_usuario_especifico' por el nombre de usuario que deseas permitir


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',{
        "products" : products
    })

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

@user_passes_test(user_is_specific_user, login_url='index')
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

@login_required
def signout (request):
    logout(request)
    return redirect("index")

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product.html', {
        "product": product
    })

@user_passes_test(user_is_specific_user, login_url='index')
def adminProduct(request, product_id):
    try:
        products = get_object_or_404(Product, pk=product_id, user=request.user)
        return render(request, 'adminProduct.html',{
            "product" : products
        })
    except:
        return redirect("admin")


@user_passes_test(user_is_specific_user, login_url='index')
def indexAdmin(request):
    products = Product.objects.all()
    return render(request, 'admin.html',{
        "products" : products
    })

    
@user_passes_test(user_is_specific_user, login_url='index')
def updateProduct(request, product_id):
    if request.method == "GET":
        try:
            products = get_object_or_404(Product, pk=product_id, user=request.user)
            form = productForm(instance=products)
            return render(request, 'updateProduct.html',{
                "product" : products,
                "form": form
            })
        except:
            return redirect("admin")
    else:
        try:
            products = get_object_or_404(Product, pk=product_id, user=request.user)
            form = productForm(request.POST, instance=products)
            form.save()
            # print(form)
            return redirect("admin")
        except:
            return render(request, 'updateProduct.html',{
            'form': productForm,
            'error': 'please provide valide data'
        })


@user_passes_test(user_is_specific_user, login_url='index')
def deleteProduct(request, product_id):
    products = get_object_or_404(Product, pk=product_id, user=request.user)
    if request.method == "POST":
        products.delete()
        return redirect("admin")
