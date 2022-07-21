from django.db.models import Sum
from home.models import Category, Donation, Institution


def donation_counter(request):
    context = {}

    try:
        context['DONATE_QUANTITY'] = int(Donation.objects.aggregate(Sum('quantity'))['quantity__sum'])
        context['DONATE_INSTITUTIONS'] = Donation.objects.filter().count()
    except TypeError:
        return {}

    return context


def foundations_info(request):
    context = {}

    context['FOUNDATIONS_0'] = Institution.objects.filter(type=0)
    context['FOUNDATIONS_1'] = Institution.objects.filter(type=1)
    context['FOUNDATIONS_2'] = Institution.objects.filter(type=2)

    return context
