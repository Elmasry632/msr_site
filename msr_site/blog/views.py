from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
# def home(request):
#      return HttpResponse("<h1>Home</h1><p>Home</p>")
def home(request):
    return render(request, 'home.html')