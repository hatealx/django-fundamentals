from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


# Create your views here.


def home(request):    
    return render(request, 'index.html')



def register(request):
   return render(request, 'register.html')


def my_login(request):
   return render(request, 'login.html')

def createTask(request):
   form =  TaskForm()
   if request.method == 'POST':
      form =  TaskForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('view-task')
      
         
   
   context =  {'form': form}
   return render(request, 'task_form.html', context = context)

def ViewTasks(request):
   tasks = Task.objects.all()
   context = {'tasks' : tasks}

   return render(request, 'view_tasks.html', context=context)


def updateTasks(request, pk):
   task = Task.objects.get(id=pk)
   form =  TaskForm(instance=task)
   if request.method == 'POST':
      form =  TaskForm(request.POST, instance=task)
      if form.is_valid():
         form.save()
         return redirect('view-task')
   
   context =  {'form': form}


   return render(request, 'update.html',context=context )


def deleteTasks(request, pk):
   task = Task.objects.get(id=pk)
   if request.method == 'POST':
      task.delete()
      return redirect('view-task')
   
   context =  {'object': task}
   return render(request, 'delete.html', context=context)