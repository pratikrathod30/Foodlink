from django.contrib.auth import authenticate,get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import ProfileSerializer

class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        expected_role = request.data.get("role")  

        if not email or not password or not expected_role:
            return Response(
                {"error": "Email, password and role are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(username=email, password=password)

        if user is None:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        if user.role != expected_role:
            return Response(
                {"error": "You are not authorized for this login"},
                status=status.HTTP_403_FORBIDDEN
            )

        if not user.is_active:
            return Response(
                {"error": "User account is disabled"},
                status=status.HTTP_403_FORBIDDEN
            )

        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "role": user.role,
            "email": user.email,
        })

User = get_user_model()


class DonorRegisterAPIView(APIView):
    def post(self, request):
        organization_name = request.data.get("name")
        email = request.data.get("email")
        password = request.data.get("password")

        if not organization_name or not email or not password:
            return Response(
                {"error": "All fields are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(email=email).exists():
            return Response(
                {"error": "Email already registered"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(
            email=email,
            password=password,
            role="DONOR",
            organization_name=organization_name
        )

        return Response(
            {
                "message": "Donor registered successfully",
                "email": user.email,
                "role": user.role
            },
            status=status.HTTP_201_CREATED
        )
class ReceiverRegisterAPIView(APIView):
    def post(self, request):
        organization_name = request.data.get("name")
        email = request.data.get("email")
        password = request.data.get("password")

        if not organization_name or not email or not password:
            return Response(
                {"error": "Please fill all fields"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(email=email).exists():
            return Response(
                {"error": "User already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(
            email=email,
            password=password,
            role="RECEIVER",
            organization_name=organization_name
        )

        return Response(
            {"message": "Receiver registered successfully"},
            status=status.HTTP_201_CREATED
        )

class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        serializer = ProfileSerializer(
            request.user,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Profile updated successfully",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
