from .models import Product, CartItem
class Carrito:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if(not carrito):
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self,producto):
        id= str(producto.id)
        if(id not in self.carrito.keys()):
            self.carrito[id] = {
                "producto_id": producto.id,
                "nombre":producto.title,
                "acumulado":producto.price,
                "cantidad":1
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.price
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self,producto):
        id = str(producto.id)
        if(id in self.carrito):
            del self.carrito[id]
            self .guardar_carrito()

    def restar(self,producto):
        id = str(producto.id)
        if(id in self.carrito.keys()):
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.price
            if self.carrito[id]["cantidad"] <= 0: 
                self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

    def agregarCarrito(self, producto):
        id = str(producto.id)

        cart_item = CartItem.objects.get(user=self.request.user, product=producto)
        cart_item.quantity += 1
        cart_item.save()
        # self.guardar_carrito()
        
    def restarCarrito(self,producto):
        id = str(producto.id)
        cart_item = CartItem.objects.get(user=self.request.user, product=producto)
        cart_item.quantity -= 1
        cart_item.save()
        if cart_item.quantity <= 0: 
            cart_item.delete()