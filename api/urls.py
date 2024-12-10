from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.InventoryListAPIView.as_view(), name='api_inventory_list'),
]