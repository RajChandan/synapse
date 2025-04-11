# Create your models here.
from django.db import models


class PricingPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_monthly = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class PlanFeature(models.Model):
    plan = models.ForeignKey(
        PricingPlan, related_name="features", on_delete=models.CASCADE
    )
    feature = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.plan.name} - {self.feature}"
