from django.db import models


class Product(models.Model):
    """
    The model describes the only existing table in the project.
    It represents a product in the system and contains 3 basic fields.

    """

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        """
        Return the string representation of the Product instances.
        """
        return self.name
