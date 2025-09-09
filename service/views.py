from django.shortcuts import render


def webinars(request):
    return render(request, "service/webinars.html")


def workshops(request):
    return render(request, "service/workshops.html")


def courses(request):
    return render(request, "service/courses.html")


def dfy_tools(request):
    return render(request, "service/dfy_tools.html")


def retainer(request):
    return render(request, "service/retainer.html")


def accelerator(request):
    return render(request, "service/accelerator.html")


def consulting_strategy(request):
    return render(request, "service/consulting_strategy.html")


def AI_integration(request):
    return render(request, "service/AI_integration.html")


def skills_training(request):
    return render(request, "service/skills_training.html")
