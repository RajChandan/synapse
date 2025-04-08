from django.urls import path
from . import views

urlpatterns = [
    path('webinars/', views.webinars, name='webinars'),
    path('workshops/', views.workshops, name='workshops'),
    path('courses/', views.courses, name='courses'),
    path('dfy-tools/', views.dfy_tools, name='dfy_tools'),
    path('retainer/', views.retainer, name='retainer'),
    path('accelerator/', views.accelerator, name='accelerator'),
]
