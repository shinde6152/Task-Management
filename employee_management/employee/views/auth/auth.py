from django.shortcuts import render
# from employee_management.employee.models.user import user


def login(request):
    return render(request, 'public/login.html')


def signup(request):

    return render(request, 'public/signup.html')
