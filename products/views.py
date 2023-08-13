from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import productForm
from .models import Product, CartItem
from django.contrib.auth.decorators import user_passes_test, login_required
from .carrito import Carrito
from django.core.files.uploadedfile import InMemoryUploadedFile

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
            product = get_object_or_404(Product, pk=product_id, user=request.user)
            form = productForm(instance=product)
            return render(request, 'updateProduct.html', {
                "product": product,
                "form": form
            })
        except:
            return redirect("admin")
    elif request.method == "POST":
        try:
            product = get_object_or_404(Product, pk=product_id, user=request.user)
            form = productForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                # Si se ha proporcionado una nueva imagen, la asignamos al campo
                new_image = form.cleaned_data.get('image')
                if isinstance(new_image, InMemoryUploadedFile):
                    product.image = new_image
                
                form.save()
                return redirect("admin")
            else:
                return render(request, 'updateProduct.html', {
                    "product": product,
                    "form": form
                })
        except:
            return render(request, 'updateProduct.html', {
                'form': productForm,
                'error': 'please provide valid data'
            })

@user_passes_test(user_is_specific_user, login_url='index')
def deleteProduct(request, product_id):
    products = get_object_or_404(Product, pk=product_id, user=request.user)
    if request.method == "POST":
        products.delete()
        return redirect("admin")


def mul(value, arg):
    return value * arg


def vista_del_carrito(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total': total,
    }

    return render(request, 'carritoVista.html', context)

def tienda(request):

    products = Product.objects.all()
    return render(request,'tienda.html',{
        'products':products
    })

def agregarProducto(request,producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id = producto_id)
    carrito.agregar(producto)
    return redirect("index")

def eliminar(request,producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("index")

def restar(request,producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("index")

def limpiar(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("index")

def guardar_carrito(request):
    if request.method == 'POST':
        carrito = Carrito(request)
        for producto_id, producto_info in carrito.carrito.items():
            producto = Product.objects.get(id=producto_info["producto_id"])
            cantidad = producto_info["cantidad"]
            
            # Buscar si ya existe un registro para este producto en el carrito del usuario
            cart_item, created = CartItem.objects.get_or_create(user=request.user, product=producto)
            
            # Si ya existe, simplemente actualiza la cantidad
            if not created:
                cart_item.quantity += cantidad
                cart_item.save()
            else:
                cart_item.quantity = cantidad
                cart_item.save()

        carrito.limpiar()

    return redirect("carrito")


def eliminarCarrito(request, producto_id):
    carrito = Carrito(request)
    producto = CartItem.objects.get(id = producto_id)
    producto.delete()
    return redirect("carrito")

def agregarCarrito(request,producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=producto_id)
    carrito.agregarCarrito(producto)  # Asegúrate de tener un método "aumentar" en tu clase Carrito
    return redirect("carrito")

def restarCarrito(request,producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=producto_id)
    carrito.restarCarrito(producto)  # Asegúrate de tener un método "aumentar" en tu clase Carrito
    return redirect("carrito")
