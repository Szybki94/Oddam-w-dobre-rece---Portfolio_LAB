from django.db.models import Sum
from home.models import Donation


def donation_counter(request):
    context = {}

    try:
        context['DONATE_QUANTITY'] = int(Donation.objects.aggregate(Sum('quantity'))['quantity__sum'])
        context['DONATE_INSTITUTIONS'] = Donation.objects.filter().count()
    except TypeError:
        return {}

    return context
