from home.models import User, Category, Institution
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


CATEGORY_CHOICES = tuple([(category.id, f"{category.name}") for category in Category.objects.all()])
INSTITUTION_CHOICES = tuple([(institution.id, f'Fundacja "{institution.name}"')
                             for institution in Institution.objects.all()])


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]
        widgets = {

            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Imię",
            }),

            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nazwisko",
            }),
            "email": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Email",
            }),
        }

    # Ponieważ pola password1 i password2 nie są polami formularza, zrobiłem takie Fiku-miku (Stack Overflow)
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Hasło'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Powtórz hasło'})

    def clean_email(self):
        email = self.cleaned_data["email"]

        if "@" not in email:
            raise ValidationError("Wprowadź prawidłowy adres email")
        else:
            return email

    def clean_password2(self):
        password_1 = self.cleaned_data["password1"]
        password_2 = self.cleaned_data["password2"]

        if password_1 != password_2:
            raise ValidationError("Drugie hasło nie jest takie samo jak pierwsze")
        else:
            return password_2


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


class DonationForm(forms.Form):

    category = forms.MultipleChoiceField(choices=CATEGORY_CHOICES, widget=forms.CheckboxSelectMultiple(
        attrs={
            "type": "description",
        }))

    amount = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            "type": "number",
            "step": "1",
            "min": "1",
        }))

    institution = forms.MultipleChoiceField(choices=INSTITUTION_CHOICES, widget=forms.RadioSelect(
        attrs=
        {
            "type": "radio",
        }))

    address = forms.CharField(widget=forms.TextInput(attrs={"type": "text"}))
    city = forms.CharField(widget=forms.TextInput(attrs={"type": "text"}))
    postcode = forms.CharField(widget=forms.TextInput(attrs={"type": "text"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"type": "phone"}))
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={"type": "date"}))
    more_info = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}))
