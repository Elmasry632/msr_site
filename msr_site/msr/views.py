from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from .models import *
from .forms import *
# Create your views here.


def msr(request):
    boards = Task_board.objects.all()
    return render(request,'index.html',{'boards':boards})

    # first option dont use html file
    # ----------------------?
    # boards_list = []
    # for task_board in boards:
    #     boards_list.append(task_board.project_name)
    #     responce_html = '<br />'.join(boards_list)
    #     # print(board.project_name)
    # return HttpResponse(responce_html) 

    # second option use html file
# ------------------------------------------------------------------------------------------
def board_topics(request, board_id):
    # try:
    #     board = Task_board.objects.get(pk=board_id)

    # except Task_board.DoesNotExist:
    #     raise Http404
    board = get_object_or_404(Task_board, pk=board_id)
    # form = addNewProgect()
    return render(request, 'topics.html', {'board': board})

def task_board(request):
    task_desc_board = Task_desc.objects.all()
    # task_desc = get_object_or_404(Task_desc)
    return render(request, 'task_board.html',{'task_desc_board':task_desc_board})

def test_board (request):
    test_boards = test.objects.all()
    return render(request,'add_project.html',{'test_boards':test_boards})




