from django.urls import path
from . import views
urlpatterns = [
    path("",views.AddTask,name="Add_Task"),
    path("edit/<int:id>",views.EditTask,name="Edit_Task"),
    path("delete/<int:id>",views.DeleteTask,name="delete_Task"),
]
