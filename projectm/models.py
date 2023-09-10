from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=50, help_text="Project Name")
    creation_time = models.DateTimeField(auto_now_add=True, help_text="Project creation time.")

class Task(models.Model):
    title = models.CharField(max_length=50, help_text="Task Title")
    description = models.TextField(help_text="Task Description")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, help_text="Project")
    time_estimate = models.IntegerField(help_text="Task Time Estimate")

