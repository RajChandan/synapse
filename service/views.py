from django.shortcuts import render

def webinars(request):
    return render(request, 'service/webinars.html')

def workshops(request):
    return render(request, 'service/workshops.html')

def courses(request):
    return render(request, 'service/courses.html')

def dfy_tools(request):
    return render(request, 'service/dfy_tools.html')

def retainer(request):
    return render(request, 'service/retainer.html')

def accelerator(request):
    return render(request, 'service/accelerator.html')
