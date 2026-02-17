from django.urls import path
from .views import (
    CreateFoodRequestAPIView,
    ApproveFoodRequestAPIView,
    RejectFoodRequestAPIView,
    ReceiverDashboardAPIView,
    ReceiverReceivedHistoryAPIView,
    MarkCollectedAPIView,
    DonorRequestsAPIView
)

urlpatterns = [
    path('create/', CreateFoodRequestAPIView.as_view(), name='create-food-request'),
    path('<int:pk>/approve/', ApproveFoodRequestAPIView.as_view(), name='approve-food-request'),
    path('<int:pk>/reject/', RejectFoodRequestAPIView.as_view(), name='reject-food-request'),
    path('<int:pk>/collected/', MarkCollectedAPIView.as_view(), name='mark-collected'),
    path('donor/', DonorRequestsAPIView.as_view(), name='donor-requests'),
    path('dashboard/', ReceiverDashboardAPIView.as_view(), name='receiver-dashboard'),
    path('received/', ReceiverReceivedHistoryAPIView.as_view(), name='receiver-received-history'),
]
