from django.shortcuts import render

# Create your views here.


def chatbot_home(request):
    return render(request, "chatbot/chatbot_home.html")
