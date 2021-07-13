from django.db import models

# Create your models here.

class Task(models.Model):
  title = models.CharField(max_length=30)
  completed = models.BooleanField(default=False, blank=True)
  class Meta:
    app_label = 'server.api'
