from django.shortcuts import render

def manager_tasks(request):
    return render(request, 'manager/tasks.html')