from django.urls import path
from . import views

urlpatterns = [
    path('', views.industry_list, name='industry_list'),
    path('<slug:slug>/', views.industry_detail, name='industry_detail'),
]
