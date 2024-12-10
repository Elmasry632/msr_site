from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task_board, Task_desc
from .forms import * 
from django.http import Http404
def msr(request):
    boards = Task_board.objects.all()
    return render(request, "index.html", {"boards": boards})
def task_board(request, board_id):
    board = get_object_or_404(Task_board, pk=board_id)
    tasks = Task_desc.objects.filter(board=board)
    return render(request, "topics.html", {"board": board, "tasks": tasks})
@login_required
def add_project(request, board_id):
    board = get_object_or_404(Task_board, pk=board_id) if board_id else None
    try:
        task_desc = get_object_or_404(Task_desc, pk=board_id)
    except Http404:
        task_desc = None
    if request.method == "POST":
        form = AddProjectForm(request.POST)
        if form.is_valid(): 
            Task_board.objects.create(project_name=form.cleaned_data["project_name"],
            desc_project=form.cleaned_data["description"],
            created_by=request.user, )
            Task_desc.objects.create(task_name=form.cleaned_data["taskname"]
                                     , responsible=form.cleaned_data["Responsiple"]
                                     , task_desc=form.cleaned_data["task_description"]
                                     , board=board)
            messages.success(request, "Project created successfully!")
            return redirect("task_board", board_id=board_id) 
    else:
        form = AddProjectForm()
    return render(request, "add_project.html", {"form": form, "board": board,"task_desc": task_desc})