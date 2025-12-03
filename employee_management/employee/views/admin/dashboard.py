from django.shortcuts import render


def admin_dasboard(request):
    return render(request, 'admin/dashboard.html')
