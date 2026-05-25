from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Todo

@login_required
def index(request):
    if request.method == "POST":
        title = request.POST.get("title")
        priority = request.POST.get("priority")
        if title:
            # priorityが渡されていない場合はモデルのデフォルト値が使われます
            Todo.objects.create(title=title, priority=priority or Todo.Priority.MIDDLE)
        return redirect("index")
    
    todos = Todo.objects.all()
    return render(request, "tasks/index.html", {
        "todos": todos,
        "priorities": Todo.Priority.choices
    })


@login_required
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        todo.delete()
    return redirect("index")

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("index")
    else:
        form = AuthenticationForm()
    return render(request, "tasks/login.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        auth_logout(request)
        return redirect("login")
    return redirect("index")
