from django.db import models

class Todo(models.Model):
    class Priority(models.TextChoices):
        HIGH = 'high', '高'
        MIDDLE = 'middle', '中'
        LOW = 'low', '低'

    title = models.CharField(max_length=200)
    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MIDDLE,
    )

    def __str__(self):
        return f"{self.title} ({self.get_priority_display()})"

