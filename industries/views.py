from django.shortcuts import render, get_object_or_404
from .models import Industry

def industry_list(request):
    industries = Industry.objects.filter(is_active=True)
    return render(request, 'industries/industry_list.html', {'industries': industries})

def industry_detail(request, slug):
    industry = get_object_or_404(Industry, slug=slug, is_active=True)
    return render(request, 'industries/industry_detail.html', {'industry': industry})
