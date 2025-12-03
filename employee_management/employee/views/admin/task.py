from django.shortcuts import render


def admin_task(request):
    return render(request, 'admin/tasks.html')
