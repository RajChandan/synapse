from django.contrib.auth.models import User
from django.db import models


class InsiderTier(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    benefits = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class InsiderSubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tier = models.ForeignKey(InsiderTier, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.tier.name}"
