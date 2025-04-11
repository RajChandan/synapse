from django.urls import path

from . import views

urlpatterns = [
    path("", views.insider_home, name="insider_home"),
    path("subscribe/<int:tier_id>/", views.subscribe, name="subscribe"),
]
