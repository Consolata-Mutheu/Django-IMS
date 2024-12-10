from django.test import TestCase
from django.urls import reverse
from .models import Inventory, Supplier

class InventoryTestCase(TestCase):
    def setUp(self):
        # Create sample data for testing
        supplier = Supplier.objects.create(name='Supplier A')
        Inventory.objects.create(
            name='Item 1',
            description='Description for Item 1',
            note='Note for Item 1',
            stock=10,
            availability=True,
            supplier=supplier
        )

    def test_inventory_list_page_status(self):
        # Access the inventory list page
        response = self.client.get(reverse('inventory_list'))

        # Check if the page returns status code 200
        self.assertEqual(response.status_code, 200)

        # Check if added data is present in the response content
        self.assertContains(response, 'Item 1')
        self.assertContains(response, 'Supplier A')

    def test_inventory_detail_page_status(self):
            # Get the ID of the created inventory object
        inventory = Inventory.objects.get(name='Item 1')

        # Access the inventory detail page for the added item
        response = self.client.get(reverse('inventory_detail', kwargs={'pk': inventory.pk}))

        # Check if the page returns status code 200
        self.assertEqual(response.status_code, 200)

        # Check if the added data details are present in the response content
        self.assertContains(response, 'Item 1')
        self.assertContains(response, 'Description for Item 1')
        self.assertContains(response, 'Note for Item 1')

    def test_api_inventory_page_status(self):
        # Access the API endpoint for inventory
        response = self.client.get('/api/inventory/')

        # Check if the API endpoint returns status code 200
        self.assertEqual(response.status_code, 200)
