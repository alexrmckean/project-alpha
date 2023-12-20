from django.urls import path
from projects.views import show_project_list, show_project

urlpatterns = [
    path("", show_project_list, name="list_projects"),
    path("<int:id>/", show_project, name="show_project"),
]
