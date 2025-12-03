from django.shortcuts import render


def admin_user(request):
    return render(request, 'admin/users.html')
