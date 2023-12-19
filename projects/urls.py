from django.urls import path
from projects.views import show_project_list

urlpatterns = [
    path("", show_project_list, name="list_projects")
]
