from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.

class Cabinet(models.Model):
    number = models.CharField(max_length=32, null=True, blank=True)
    opt = models.CharField(max_length=32, null=True, blank=True)


class Workspace(models.Model):
    number = models.CharField(max_length=32, null=True, blank=True)
    opt = models.CharField(max_length=32, null=True, blank=True)
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE)


class WorkspaceReservation(models.Model):
    time_from = models.DateTimeField()
    time_to = models.DateTimeField()
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)