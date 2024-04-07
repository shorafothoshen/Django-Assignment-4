from django.shortcuts import render
from add_Category.models import CategoryModel
def Home(request):
    task=CategoryModel.objects.all()
    return render(request,"show_task.html",{"task":task})