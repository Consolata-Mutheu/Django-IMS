from django.contrib import admin

# Register your models here.
from .models import Inventory, Supplier

admin.site.register(Inventory)
admin.site.register(Supplier)