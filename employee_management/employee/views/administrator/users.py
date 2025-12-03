from django.shortcuts import render

def administrator_users(request):
    return render(request, 'administrator/users.html')