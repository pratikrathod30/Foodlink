from rest_framework import generics, permissions
from .models import Donation
from .serializers import DonationSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class AddDonationAPIView(generics.CreateAPIView):
    serializer_class = DonationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(donor=self.request.user)


class AvailableDonationsAPIView(generics.ListAPIView):
    serializer_class = DonationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Donation.objects.filter(status="available")

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


class DonorDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        total_donations = Donation.objects.filter(donor=user).count()
        available_donations = Donation.objects.filter( donor=user, status="available").count()
        requested_donations = Donation.objects.filter(donor=user, status="requested").count()
        completed_donations = Donation.objects.filter(donor=user, status="completed").count()

        return Response({
            "total_donations": total_donations,
            "available_donations": available_donations,
            "requested_donations": requested_donations,
            "completed_donations": completed_donations,
        })
    
class DonationHistoryAPIView(generics.ListAPIView):
    serializer_class = DonationSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Donation.objects.filter(
            donor=self.request.user
        ).order_by('-created_at')
