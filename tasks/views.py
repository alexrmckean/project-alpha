from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm
from tasks.models import Task
from projects.models import Project

# Create your views here.
@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            receipt = form.save()
            receipt.owner = request.user
            receipt.save()
            return redirect("list_projects")

    else:
        form = TaskForm()

    context = {"form": form}

    return render(request, "tasks/create.html", context)


@login_required
def show_task_list(request):
  task_list = Task.objects.filter(assignee=request.user)
  context = {
    "task_list": task_list,
  }
  return render(request, "tasks/list.html", context)
