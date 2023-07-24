from django.forms import ModelForm 
from .models import Product


class productForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "price",
            "exist",
            "description",
            "image"
        ]