from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'core/home.html')

def about(request):
    return render(request,'core/about.html')


def contact(request):
    return render(request,'core/contact.html')

def terms_of_service(request):
    return render(request,'core/terms_of_service.html')

def privacy_policy(request):
    return render(request,'core/privacy_policy.html')

def page_not_found_view(request, exception):
    return render(request,'core/404.html', status=404)
