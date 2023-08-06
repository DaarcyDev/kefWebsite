from django.db import models
from django.contrib.auth.models import User

CATEGORIA_CHOICES = [
    ('Ropa', 'Ropa'),
    ('Accesorios', 'Accesorios'),
    ('Deporte', 'Deporte'),
    ('Zapatos', 'Zapatos'),
    ('RopaInterior', 'RopaInterior'),
    ('RopaBaño', 'RopaBaño'),
    ('Camisa', 'Camisa'),
    ('Pantalones', 'Pantalones'),
    ('Chaquetas', 'Chaquetas'),
    ('ZapatosVestir', 'ZapatosVestir'),
    ('Trajes', 'Trajes'),
    ('Jeans', 'Jeans'),
    ('Polos', 'Polos'),
    ('Bolsos', 'Bolsos'),
    ('Vestidos', 'Vestidos'),
    ('Faldas', 'Faldas'),
    ('Blusas', 'Blusas'),
    ('ZapatosTacon', 'ZapatosTacon'),
    ('Pijamas', 'Pijamas'),
    ('Playeras', 'Playeras'),
]

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField(blank=True)
    exist = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='productImages/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True)
    is_male = models.BooleanField(default=False)
    is_female = models.BooleanField(default=False)
    is_child = models.BooleanField(default=False)
    category = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='Ropa') 
 

    def __str__(self):
        return self.title + " - " + self.user.username


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    # Agrega cualquier otro campo necesario, como precio unitario, total, etc.

    def subtotal(self):
        return self.product.price * self.quantity
