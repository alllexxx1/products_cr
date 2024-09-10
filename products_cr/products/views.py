from rest_framework import generics

from products_cr.products.models import Product
from products_cr.products.serializers import ProductSerializer


class ProductAPIList(generics.ListCreateAPIView):
    """
    Product API view for listing a queryset or creating the Product model instance.

    It uses ListCreateAPIView to keep the code short and neat.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
