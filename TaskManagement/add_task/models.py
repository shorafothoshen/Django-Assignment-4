from django.db import models

# Create your models here.
class TaskModel(models.Model):
    taskTitle=models.CharField(max_length=70)
    taskDescription=models.TextField()
    taskDate=models.DateField()
    is_completed=models.BooleanField(default=False)

    def __str__(self):
        return self.taskTitle