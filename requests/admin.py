from django.contrib import admin
from .models import FoodRequest

@admin.register(FoodRequest)
class FoodRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'donation', 'receiver', 'status', 'requested_at')
    list_filter = ('status',)
