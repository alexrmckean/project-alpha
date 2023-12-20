from django.db import models
from django.contrib.auth.models import User
from projects.models import Project
from django.utils import timezone


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(default=timezone.now)
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(
       Project,
       related_name="tasks",
       on_delete=models.CASCADE,
    )
    assignee = models.ForeignKey(
        User,
        null = True,
        related_name = "tasks",
        on_delete=models.CASCADE,
    )
