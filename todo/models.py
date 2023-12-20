from django.db import models
from django.utils import timezone  # Import the timezone module

class Todo(models.Model):
    text = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)  # Add a new field for task creation time

    def __str__(self):
        return self.text

