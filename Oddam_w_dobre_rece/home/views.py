from django.views.generic import View
from django.shortcuts import render

# Create your views here.


# This view is only for testing view
class TestView(View):
    def get(self, request):
        return render(request, "index.html", {})
