from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register),
    path('', views.home),  
    path('create_task', views.createTask, name='create_task'),
    path('view-task', views.ViewTasks, name='view-task'), 
    path('update-task/<str:pk>', views.updateTasks, name='update-task'),
    path('delete-task/<str:pk>', views.deleteTasks, name='delete-task'),
    path('register', views.register, name='register'),
    path('my-login', views.login, name='my-login'),

] 