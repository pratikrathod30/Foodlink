from django.shortcuts import render

def home(request):
    return render(request, "home.html")
def how_it_works(request):
    return render(request, "HowItWorks.html")
def donor_login(request):
    return render(request, "donor/DonorLogin.html")
def donor_register(request):
    return render(request, "donor/DonorRegister.html")
def receiver_login(request):
    return render(request, "receiver/ReceiverLogin.html")
def receiver_register(request):
    return render(request, "receiver/ReceiverRegister.html")
def donor_profile(request):
    return render(request, "donor/profile.html")
def donor_dashboard(request):
    return render(request, "donor/dashboard.html")
def donor_add_donation(request):
    return render(request, "donor/add_donation.html")
def donor_add_donation(request):
    return render(request, "donor/add_donation.html")
def donor_history(request):
    return render(request, "donor/history.html")
def donor_requests(request):
    return render(request, "donor/requests.html")
def receiver_profile(request):
    return render(request, "receiver/profile.html")
def receiver_dashboard(request):
    return render(request, "receiver/dashboard.html")
def receiver_available_food(request):
    return render(request, "receiver/available_food.html")
def receiver_history(request):
    return render(request, "receiver/history.html")

