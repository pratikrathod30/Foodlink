from django.urls import path
from .views import (home,how_it_works,
                    donor_login,donor_register,
                    receiver_login,receiver_register,
                    donor_profile,donor_dashboard,donor_add_donation,donor_history,donor_requests,
                    receiver_profile,receiver_dashboard,receiver_available_food,receiver_history)
urlpatterns = [
    path("", home, name="home"),
    path("how-it-works/", how_it_works, name="how_it_works"),
    path("donor/login/", donor_login),
    path("donor/register/", donor_register),
    path("receiver/login/", receiver_login),
    path("receiver/register/", receiver_register),
    path("donor/profile/", donor_profile),
    path("donor/dashboard/", donor_dashboard),
    path("donor/add-donation/", donor_add_donation),
    path("donor/history/", donor_history),
    path("donor/requests/", donor_requests),
    path("receiver/profile/", receiver_profile),
    path("receiver/dashboard/", receiver_dashboard),
    path("receiver/available-food/", receiver_available_food),
    path("receiver/history/", receiver_history),

]
