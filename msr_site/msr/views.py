from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task_board, Task_desc
from .forms import AddProjectForm  # تأكد أن النموذج معرف بشكل صحيح

# عرض جميع لوحات المشاريع (Task Boards)
def msr(request):
    boards = Task_board.objects.all()
    return render(request, "index.html", {"boards": boards})

# عرض جميع المهام المرتبطة بلوحة معينة
def task_board(request, board_id):
    board = get_object_or_404(Task_board, pk=board_id)
    tasks = Task_desc.objects.filter(board=board)
    return render(request, "topics.html", {"board": board, "tasks": tasks})

# إضافة مشروع جديد إلى لوحة المشاريع
@login_required
def add_project(request, board_id=None):
    # إذا كان هناك `board_id`، جلب اللوحة أو عرض خطأ 404
    board = get_object_or_404(Task_board, pk=board_id) if board_id else None

    if request.method == "POST":
        # تمرير البيانات القادمة من النموذج
        form = AddProjectForm(request.POST)
        if form.is_valid():  # تحقق من صلاحية النموذج
            # إنشاء مشروع جديد
            Task_board.objects.create(
                project_name=form.cleaned_data["project_name"],
                desc_project=form.cleaned_data["description"],  # استخدام الحقل الصحيح
                created_by=request.user,  # المستخدم الحالي
            )
            messages.success(request, "Project created successfully!")
            return redirect("task_board", board_id=board_id)  # إعادة التوجيه إلى صفحة المشاريع (msr)
    else:
        # إذا لم يتم إرسال POST، أنشئ نموذجًا فارغًا
        form = AddProjectForm()

    # تمرير النموذج واللوحة (إذا كانت موجودة) إلى القالب
    return render(request, "add_project.html", {"form": form, "board": board})
