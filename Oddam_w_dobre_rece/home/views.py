from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.shortcuts import render, redirect, HttpResponse


from.forms import LoginForm

# Create your views here.


# This view is only for testing view
class HomeView(View):
    def get(self, request):
        return render(request, 'home.html', {})


class LoginView(View):
    context = {"form": LoginForm}

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponse("Już jesteś zalogowany")
        return render(request, "login.html", self.context)


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html', {})

    def post(self, request):
        context = {}
        name = request.POST["name"]
        surname = request.POST["surname"]
        email = request.POST["email"]
        password1 = request.POST["password"]
        password2 = request.POST["password2"]
        email_check = User.objects.filter(email=email).first()
        if email_check:
            context['register_message'] = "Użytkownik o podanym adresie e-mail już istnieje"
            return render(request, "register.html", context)
        if "@" not in email:
            context['register_message'] = "Podano zły adres email"
            return render(request, "register.html", context)
        if password1 != password2:
            context['register_message'] = "Hasła nie są zgodne"
            return render(request, "register.html", context)
        new_user = User.objects.create_user(first_name=name, last_name=surname, email=email, password=password1)
        new_user.save()
        return redirect("home:login")



class DonateView(View):
    def get(self, request):
        return render(request, 'donate_form.html', {})


# Temporary View it will be part POST metod of class aboce
class ConfirmationTemporary(View):
    def get(self, request):
        return render(request, 'donate_form_confirmation.html', {})
