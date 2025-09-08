from django.urls import path
from . import views


urlpatterns = [
    path("intell_copilot/", views.intell_copilot, name="intell_copilot"),
    path("chat_assistant/", views.chat_assistant, name="chat_assistant"),
    path(
        "workflow_orchestrator/",
        views.workflow_orchestrator,
        name="workflow_orchestrator",
    ),
]
