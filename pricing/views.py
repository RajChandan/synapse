from django.shortcuts import render

from .models import PricingPlan


def pricing_table(request):
    plans = PricingPlan.objects.filter(is_active=True).prefetch_related("features")
    return render(request, "pricing/pricing_table.html", {"plans": plans})
