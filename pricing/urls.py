from django.urls import path

from . import views

urlpatterns = [
    path("", views.pricing_table, name="pricing"),
]
