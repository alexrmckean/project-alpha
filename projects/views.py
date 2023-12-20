from django.shortcuts import render, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm
from django.forms import ModelForm


# Create your views here.
@login_required
def show_project_list(request):
  project_list = Project.objects.filter(owner=request.user)
  context = {
    "project_list": project_list,
  }
  return render(request, "projects/list.html", context)


@login_required
def show_project(request, id):
  project = Project.objects.get(id=id)
  context = {
    "project": project,
  }
  return render(request, "projects/detail.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.owner = request.user
            receipt.save()
            return redirect("list_projects")

    else:
        form = ProjectForm()

    context = {"form": form}

    return render(request, "projects/create.html", context)
