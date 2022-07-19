from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View


from.forms import LoginForm, RegistrationForm

# Create your views here.


# This view is only for testing view
class HomeView(View):
    def get(self, request):
        return render(request, 'home.html', {})


class LoginView(View):
    context = {"form": LoginForm}

    def get(self, request):
        return render(request, "login.html", self.context)


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
