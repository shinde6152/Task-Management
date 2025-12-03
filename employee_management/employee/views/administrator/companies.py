from django.shortcuts import render


def administrator_companies(request):
    return render(request, 'administrator/companies.html')