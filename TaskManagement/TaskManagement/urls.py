
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Home,name="showtask"),
    path("add_Category/",include("add_Category.urls")),
    path("add_Task/",include("add_task.urls")),
]
