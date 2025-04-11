from datetime import timedelta, date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import InsiderTier, InsiderSubscription


def insider_home(request):
    tiers = InsiderTier.objects.filter(is_active=True)
    return render(request, "insider/insider_home.html", {"tiers": tiers})


@login_required
def subscribe(request, tier_id):
    tier = get_object_or_404(InsiderTier, id=tier_id)
    # Create a dummy subscription (simulate Stripe/PayPal integration here)
    InsiderSubscription.objects.update_or_create(
        user=request.user,
        defaults={
            "tier": tier,
            "start_date": date.today(),
            "end_date": date.today() + timedelta(days=30),
            "is_active": True,
        },
    )
    return redirect("insider_home")
