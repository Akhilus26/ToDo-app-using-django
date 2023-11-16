from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

def home(request):
    todo_data = Todo.objects.all()
    if todo_data.exists():
        return render(request, 'index.html', {"todos" : todo_data})
    else:
        return render(request, 'index.html')

def create(request):
    if request.method == "POST":
        todo_name = request.POST.get('todo_name')
        todo_obj = Todo(todo_name=todo_name)
        todo_obj.save()
        return redirect('/')


def edit(request, id):
    todo_to_update = Todo.objects.get(id=id)
    if todo_to_update.status == True:
        todo_to_update.status = False
    else:
        todo_to_update.status = True
    todo_to_update.save()
    return redirect('/')
