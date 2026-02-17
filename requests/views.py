from rest_framework import generics, permissions
from .models import FoodRequest
from .serializers import FoodRequestSerializer
from donations.models import Donation
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

class CreateFoodRequestAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        donation_id = request.data.get("donation_id")
        receiver_location = request.data.get("receiver_location")

        if not donation_id or not receiver_location:
            return Response(
                {"detail": "donation_id and receiver_location required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        donation = get_object_or_404(
            Donation,
            id=donation_id,
            status="available"
        )

        if FoodRequest.objects.filter(
            donation=donation,
            receiver=request.user
        ).exists():
            return Response(
                {"detail": "Already requested"},
                status=status.HTTP_400_BAD_REQUEST
            )

        food_request = FoodRequest.objects.create(
            donation=donation,
            receiver=request.user,
            receiver_location=receiver_location
        )

        serializer = FoodRequestSerializer(food_request)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    
class DonorRequestsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        requests = FoodRequest.objects.filter(
            donation__donor=request.user
        ).select_related("donation", "receiver")

        serializer = FoodRequestSerializer(requests, many=True)
        return Response(serializer.data)
class ApproveFoodRequestAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        food_request = get_object_or_404(FoodRequest, pk=pk)

        if food_request.donation.donor != request.user:
            return Response(
                {"detail": "Not authorized"},
                status=status.HTTP_403_FORBIDDEN
            )

        food_request.status = "approved"
        food_request.save()

        donation = food_request.donation
        donation.status = "requested"
        donation.save()

        return Response(
            {"detail": "Request approved"},
            status=status.HTTP_200_OK
        )



class RejectFoodRequestAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        food_request = get_object_or_404(FoodRequest, pk=pk)

        if food_request.donation.donor != request.user:
            return Response(
                {"detail": "Not authorized"},
                status=status.HTTP_403_FORBIDDEN
            )

        food_request.status = "rejected"
        food_request.save()

        return Response(
            {"detail": "Request rejected"},
            status=status.HTTP_200_OK
        )


class ReceiverDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user  # receiver

        available_donations = Donation.objects.filter(
            status="available"
        ).count()

        total_requests = FoodRequest.objects.filter(
            receiver=user
        ).count()

        collected_requests = FoodRequest.objects.filter(
            receiver=user,
            status="collected"
        ).count()

        return Response({
            "available_donations": available_donations,
            "total_requests": total_requests,
            "collected_requests": collected_requests,
        })

class ReceiverReceivedHistoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        received = FoodRequest.objects.filter(
            receiver=request.user,
            status="collected"
        ).select_related("donation", "donation__donor")

        serializer = FoodRequestSerializer(received, many=True)
        return Response(serializer.data)

class MarkCollectedAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        food_request = get_object_or_404(FoodRequest, pk=pk)

        if food_request.donation.donor != request.user:
            return Response(
                {"detail": "Not authorized"},
                status=status.HTTP_403_FORBIDDEN
            )

        if food_request.status != "approved":
            return Response(
                {"detail": "Only approved requests can be marked as collected"},
                status=status.HTTP_400_BAD_REQUEST
            )

        food_request.status = "collected"
        food_request.save()

        donation = food_request.donation
        donation.status = "completed"
        donation.save()

        return Response(
            {"detail": "Food marked as collected"},
            status=status.HTTP_200_OK
        )
