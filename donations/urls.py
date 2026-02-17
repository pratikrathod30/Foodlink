from django.urls import path
from .views import (
    AddDonationAPIView,
    AvailableDonationsAPIView,
    DonorDashboardAPIView,
    DonationHistoryAPIView,
)

urlpatterns = [
    path('add/', AddDonationAPIView.as_view(), name='add-donation'),
    path('available/', AvailableDonationsAPIView.as_view(), name='available-donations'),
    path('dashboard/', DonorDashboardAPIView.as_view(), name='donor-dashboard'),
    path('history/', DonationHistoryAPIView.as_view(), name='donation-history'),
]
