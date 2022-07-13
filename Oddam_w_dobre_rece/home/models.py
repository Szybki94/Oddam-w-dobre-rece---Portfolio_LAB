from django.contrib.auth.models import User
from django.db import models


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

