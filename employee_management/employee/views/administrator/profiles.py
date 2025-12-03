from django.shortcuts import render

def administrator_profile(request):
    return render(request, 'administrator/profile.html')