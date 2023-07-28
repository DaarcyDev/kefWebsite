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
            "image",
            "is_male",
            "is_female",
            "is_child",
            "category",
        ]