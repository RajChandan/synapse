from django.contrib import admin

from .models import InsiderTier, InsiderSubscription


@admin.register(InsiderTier)
class InsiderTierAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_active")


@admin.register(InsiderSubscription)
class InsiderSubscriptionAdmin(admin.ModelAdmin):
    list_display = ("user", "tier", "start_date", "end_date", "is_active")
    search_fields = ("user__username",)
