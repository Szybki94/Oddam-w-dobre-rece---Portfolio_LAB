from home.models import User
from django import forms


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]
        widgets = {

            "email": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Email",
            }),

            "password": forms.PasswordInput(render_value=True, attrs={
                "class": "form-control",
                "placeholder": "Hasło"
            }),
        }
