from django.shortcuts import render


# Create your views here.
def intell_copilot(request):
    return render(request, "product/intell_copilot.html")


def chat_assistant(request):
    return render(request, "product/chat_assistant.html")


def workflow_orchestrator(request):
    return render(request, "product/workflow_orchestrator.html")
