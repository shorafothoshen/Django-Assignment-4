from django.db import models
from add_task.models import TaskModel
# Create your models here.
class CategoryModel(models.Model):
    categoryName=models.CharField(max_length=30)
    addTask=models.ManyToManyField(TaskModel)

    def __str__(self):
        return self.categoryName