import os
import json

from django.test import TestCase

from products_cr.products.models import Product


def load_test_data(filename):
    """
    Function for retrieving test_data from json file.
    """

    filepath = os.path.abspath(f'products_cr/products/test_data/{filename}')
    with open(filepath, 'r') as file:
        return json.loads(file.read())


class ProductTestCase(TestCase):
    """
    Test case for checking basic Create and Read functionality.
    """

    def setUp(self):
        products_data = load_test_data('products.json')

        for product in products_data:
            Product.objects.create(
                name=product['name'],
                description=product['description'],
                price=product['price']
            )

    def test_retrieve_products(self):
        products = Product.objects.all()
        product = Product.objects.get(name='Moldex Беруши')

        self.assertEqual(products.count(), 3)
        self.assertEqual(product.description, 'Беруши с фирменным кейсом, 3 пары')
        self.assertEqual(product.price, 400)

    def test_api_endpoint(self):
        response = self.client.get('/api/products/')
        product = response.data[1]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(float(product['price']), 200.00)

    def test_post_product(self):
        post_url = '/api/products/'

        new_product_data = {
            "name": "New Test Product",
            "description": "A new test product description",
            "price": 15.99
        }

        response = self.client.post(post_url, new_product_data, format='json')
        product = Product.objects.get(name="New Test Product")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(product.description, new_product_data['description'])

    def test_post_product_invalid_data(self):
        post_url = '/api/products/'

        invalid_product_data = {
            "name": "Invalid Test Product",
            "description": "An invalid test product with negative price",
            "price": -1000
        }

        response = self.client.post(post_url, invalid_product_data, format='json')

        self.assertEqual(response.status_code, 400)
        self.assertIn('price', response.data)
