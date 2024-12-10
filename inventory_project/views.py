from django.shortcuts import render

def home(request):
    return render(request, 'inventory_project/home.html')