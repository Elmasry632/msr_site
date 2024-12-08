from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *  # يجب تعريف هذه النماذج في forms.py


# عرض جميع لوحات المشاريع (Task Boards)
def msr(request):
    boards = Task_board.objects.all()
    return render(request, "index.html", {"boards": boards})


# عرض جميع المهام المرتبطة بلوحة معينة
def task_board(request, board_id):
    board = get_object_or_404(Task_board, pk=board_id)
    tasks = Task_desc.objects.filter(board=board)
    return render(request, "topics.html", {"board": board, "tasks": tasks})


# إضافة لوحة مشروع جديدة
@login_required
def add_project(request, board_id):
    board = get_object_or_404(Task_board, pk=board_id)
    if request.method == "POST":
        form = AddProjectForm(request.POST)
        if form.is_valid():
            Task_board.objects.create(
                project_name=form.cleaned_data["project_name"],
                desc_project=form.cleaned_data["desc_project"],
                created_by=request.user,
            )
            messages.success(request, "Project created successfully!")
            return redirect("task_boards")
    else:
        form = AddProjectForm()

    return render(request, "add_project.html", {"form": form})


# إضافة مهمة جديدة إلى لوحة
# @login_required
# def add_task(request, board_id):
#     board = get_object_or_404(Task_board, pk=board_id)
#     if request.method == 'POST':
#         form = AddTaskForm(request.POST)
#         if form.is_valid():
#             Task_desc.objects.create(
#                 task_name=form.cleaned_data['task_name'],
#                 responsible=form.cleaned_data['responsible'],
#                 task_desc=form.cleaned_data['task_desc'],
#                 board=board,
#                 created_by=request.user
#             )
#             messages.success(request, "Task added successfully!")
#             return redirect('board_tasks', board_id=board.id)
#     else:
#         form = AddTaskForm()

#     return render(request, 'add_task.html', {'form': form, 'board': board})
# #


# عرض تفاصيل مهمة معينة
# def task_detail(request, task_id):
#     task = get_object_or_404(Task_desc, pk=task_id)
#     return render(request, "task_detail.html", {"task": task})
