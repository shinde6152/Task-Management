from django.shortcuts import render

def manager_team(request):
    return render(request, 'manager/team.html')