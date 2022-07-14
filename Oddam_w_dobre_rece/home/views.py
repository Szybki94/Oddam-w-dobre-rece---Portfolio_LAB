from django.views.generic import View
from django.shortcuts import render, HttpResponse

# Create your views here.


# This view is only for testing view
class HomeView(View):
    def get(self, request):
        return render(request, 'home.html', {})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html', {})


class DonateView(View):
    def get(self, request):
        return render(request, 'donate_form.html', {})
