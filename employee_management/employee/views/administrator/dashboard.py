from django.shortcuts import render

def administrator_dashboard(request):
    return render(request, 'administrator/dashboard.html')