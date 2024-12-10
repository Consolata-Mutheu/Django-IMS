from django.shortcuts import render
from .models import Inventory

def inventory_list(request):
    inventories = Inventory.objects.all()
    return render(request, 'inventory/inventory_list.html', {'inventories': inventories})

def inventory_detail(request, pk):
    inventory = Inventory.objects.get(pk=pk)
    return render(request, 'inventory/inventory_detail.html', {'inventory': inventory})