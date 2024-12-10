from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),
    path('<int:pk>/', views.inventory_detail, name='inventory_detail'),
]