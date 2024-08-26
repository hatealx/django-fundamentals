from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),  
    path('register', views.register, name='register'),
    path('my-login', views.login, name='my-login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('my-logout', views.logout, name='my-logout'),
    path('create_task', views.createTask, name='create_task'),
    path('view_task', views.viewTask, name='view_task'),
    path('update_task/<str:pk>', views.updateTask, name='update_task'),
    path('delete_task/<str:pk>', views.deleteTask, name='delete_task'),
    path('profile_management', views.profileManagement, name='profile_management'),
    path('delete_account', views.deleteAccount, name='delete_account'),

] 