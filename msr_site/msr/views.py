from django.shortcuts import render
from django.http import HttpResponse
from .models import Task_board
# Create your views here.


def msr(request):
    boards = Task_board.objects.all()

    # first option dont use html file
    # ----------------------?
    # boards_list = []
    # for task_board in boards:
    #     boards_list.append(task_board.project_name)
    #     responce_html = '<br />'.join(boards_list)
    #     # print(board.project_name)
    # return HttpResponse(responce_html) 

    # second option use html file

    return render(request,'index.html',{'boards':boards})