from django.urls import path
from .views import LoginAPIView,DonorRegisterAPIView,ReceiverRegisterAPIView,UserProfileAPIView
urlpatterns = [
    path("login/", LoginAPIView.as_view()),
    path("register/donor/", DonorRegisterAPIView.as_view()),
    path("register/receiver/", ReceiverRegisterAPIView.as_view()),
    path("profile/", UserProfileAPIView.as_view()),

]
