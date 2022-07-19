from django.contrib.auth.models import User
from django.db import models


# Import for custom_user settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _


# Custom user class
"""Declare models for YOUR_APP app."""

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=512)


class Institution(models.Model):
    CHOICES = (
        (0, "fundacja"),
        (1, "organizacja pozarządowa"),
        (2, "zbiórka lokalna"),
    )

    name = models.CharField(max_length=512)
    description = models.TextField()
    type = models.CharField(max_length=2, choices=CHOICES, default=0)
    category = models.ManyToManyField(Category, related_name='category')


class Donation(models.Model):
    quantity = models.PositiveSmallIntegerField()
    categories = models.ManyToManyField(Category, related_name='categories')
    institution = models.ForeignKey(Institution, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=512)
    phone_number = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=32)
    pick_up_date = models.DateField(blank=True, null=True)
    pick_up_time = models.TimeField(blank=True, null=True)
    pick_up_comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING)

