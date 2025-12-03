from django.shortcuts import render

def user_task(request):
    return render(request, 'user/tasks.html')