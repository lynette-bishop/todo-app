from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def index(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Todo.objects.create(title=title)
        return redirect("index")
    
    todos = Todo.objects.all()
    return render(request, "tasks/index.html", {"todos": todos})

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        todo.delete()
    return redirect("index")
