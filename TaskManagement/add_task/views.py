from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import TaskModel
# Create your views here.
def AddTask(request):
    if request.method=="POST":
        task=TaskForm(request.POST)
        if task.is_valid():
            task.save()
            return redirect("Add_Category")
    else:
        task=TaskForm()
    return render(request,"task/addTask.html",{"form":task})


def EditTask(request,id):
    postTask=TaskModel.objects.get(pk=id)
    if request.method=="POST":
        task=TaskForm(request.POST ,instance=postTask)
        if task.is_valid():
            task.save()
            return redirect("showtask")
    else:
        task=TaskForm(instance=postTask)
    return render(request,"task/addTask.html",{"form":task})

def DeleteTask(request,id):
    delete=TaskModel.objects.get(pk=id).delete()
    return redirect("showtask")