from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Donation(models.Model):

    FOOD_CATEGORY_CHOICES = (
        ('cooked', 'Cooked Food'),
        ('packed', 'Packed Food'),
        ('raw', 'Raw Ingredients'),
    )

    FOOD_TYPE_CHOICES = (
        ('veg', 'Veg'),
        ('non-veg', 'Non-Veg'),
    )

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('requested', 'Requested'),
        ('completed', 'Completed'),
    )

    donor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='donations'
    )

    food_name = models.CharField(max_length=100)
    food_category = models.CharField(
        max_length=20,
        choices=FOOD_CATEGORY_CHOICES,
        default='cooked'
    )

    food_type = models.CharField(
        max_length=10,
        choices=FOOD_TYPE_CHOICES
    )

    quantity = models.CharField(max_length=50)

    expiry_time = models.DateTimeField()
    pickup_address = models.TextField()
    notes = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.food_name} ({self.status})"
