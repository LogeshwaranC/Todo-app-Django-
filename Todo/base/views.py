from django.shortcuts import render,redirect
from . models  import Tasks
from . forms import *  # Import your Tasks model

def index(request):
    tasks = Tasks.objects.all()  
    
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/')

    context = {'tasks': tasks, 'form' : form}
    return render(request, 'base/lists.html', context)

def update_task (request,pk):
    tasks = Tasks.objects.get(id = pk)

    form = TaskForm(instance = tasks)
    if request.method =='POST':
        form = TaskForm(request.POST, instance =tasks)
        if form.is_valid():
            form.save()
            return redirect ('/')
    context ={'form': form}

    return render(request, 'base/Update_task.html', context)

def deletetask(request,pk):
    item = Tasks.objects.get(id =pk)
    if request.method =='POST':
        item.delete()
        return redirect ('/')

    context ={'item': item }
    return render(request, 'base/delete.html',context)