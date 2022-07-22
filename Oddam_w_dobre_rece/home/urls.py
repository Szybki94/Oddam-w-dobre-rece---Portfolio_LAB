from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

# VIEWS IMPORT
from .views import DonateView, HomeView, LoginView, LogoutView, RegisterView, ConfirmationTemporary

app_name = "home"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("donate/", DonateView.as_view(), name="donate"),
    path("donate-confirmation/", ConfirmationTemporary.as_view(), name="donate_confirmation"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
