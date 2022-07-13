from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

# VIEWS IMPORT
from .views import TestView

app_name = "home"

urlpatterns = [
    path("test-home/", TestView.as_view(), name="test")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
