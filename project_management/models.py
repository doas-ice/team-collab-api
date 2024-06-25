from django.db import models
from django.contrib.auth.models import User

class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ProjectMember(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Projects, related_name='members', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[
        ('Admin', 'Admin'),
        ('Member', 'Member')
    ])

    def __str__(self):
        return f"{self.user.username} - {self.project.name}"
