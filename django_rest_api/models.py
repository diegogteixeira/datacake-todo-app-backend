from django.db import models

class Task(models.Model):
  description = models.CharField(max_length=100)
  done = models.BooleanField(default=False, blank=True)

  def __str__(self):
    return self.description