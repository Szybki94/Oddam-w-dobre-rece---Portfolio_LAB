from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View

from .models import User

from.forms import LoginForm, RegistrationForm

# Create your views here.


# This view is only for testing view
class HomeView(View):
    def get(self, request):
        return render(request, 'home.html', {})


class LoginView(View):

    def get(self, request):
        form = LoginForm
        return render(request, "login.html", {"form": form})

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        user_check = User.objects.filter(email=email).first()
        if user_check is None:
            messages.error(request, "Użytkownik o podanym adresie e-mail nie istnieje- stwórz konto")
            return redirect("home:register")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Udało się zalogować")
            return redirect("home:home")
        else:
            messages.error(request, "Podane hasło jest nieprawidłowe")
            return redirect("home:login")


class RegisterView(View):
    def get(self, request):
        form = RegistrationForm
        return render(request, 'register.html', {"form": form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Stworzono konto dla użytkownika - {form.cleaned_data['email']}")
            return redirect("home:login")
        else:
            return render(request, "register.html", {"form": form})



class DonateView(View):
    def get(self, request):
        return render(request, 'donate_form.html', {})


# Temporary View it will be part POST metod of class aboce
class ConfirmationTemporary(View):
    def get(self, request):
        return render(request, 'donate_form_confirmation.html', {})
