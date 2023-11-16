from django.db import models
from django.db import models

# Create your models here.

class Todo(models.Model):
    todo_name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)