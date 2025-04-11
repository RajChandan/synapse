from django.contrib import admin

from .models import PricingPlan, PlanFeature


class PlanFeatureInline(admin.TabularInline):
    model = PlanFeature
    extra = 1


@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_monthly", "is_featured", "is_active")
    inlines = [PlanFeatureInline]


admin.site.register(PlanFeature)
