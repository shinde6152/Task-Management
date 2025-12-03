from django.shortcuts import render


def admin_profile(request):
    return render(request, 'admin/profile.html')
