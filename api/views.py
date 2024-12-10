from rest_framework import generics
from inventory.models import Inventory
from .serializers import InventorySerializer

class InventoryListAPIView(generics.ListAPIView):
    serializer_class = InventorySerializer

    def get_queryset(self):
        queryset = Inventory.objects.all()
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset