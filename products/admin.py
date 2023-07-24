from django.contrib import admin
from .models import Product

class productAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)

# Register your models here.

admin.site.register(Product, productAdmin)

