from django.urls import path
from projects.views import show_project_list, show_project, create_project

urlpatterns = [
    path("", show_project_list, name="list_projects"),
    path("<int:id>/", show_project, name="show_project"),
    path("create/", create_project, name="create_project"),
]
