from rest_framework import serializers
from products_cr.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer class for serializing Product model data.

    This serializer converts Product model instances into
    JSON format and specifies the fields to include.
    """

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']

    def validate_price(self, value):
        """
        The custom validator ensures that given price is a positive number.

        Blank "name" field validation is ensured by DRF by default.
        """
        if value <= 0:
            raise serializers.ValidationError('The price must be a positive number')
        return value
