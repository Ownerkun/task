from django.shortcuts import render, redirect

def task_list(request):
    return render(request, 'mysite/task_list.html')