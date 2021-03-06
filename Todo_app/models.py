from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    added_date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=200)
    def __str__(self):
        return self.text
