from django.db import models
from django.conf import settings
from donations.models import Donation

User = settings.AUTH_USER_MODEL

class FoodRequest(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('collected', 'Collected'),
    )

    donation = models.ForeignKey(
        Donation,
        on_delete=models.CASCADE
    )

    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    receiver_location = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    requested_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.receiver} -> {self.donation}"
