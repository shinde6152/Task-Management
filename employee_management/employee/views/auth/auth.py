from django.shortcuts import render
from ...validations.signupvalidation import validate_signup_data
from ...models.user import user
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password


def login(request):
    return render(request, 'public/login.html')


def signup(request):
    if request.method == 'POST':
        fullName = request.POST.get('fullName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        terms = request.POST.get('terms')

        try:
            validate_signup_data(fullName, email, password, confirmPassword, terms)

            # Hash Password.
            hashed_password = make_password(password)

            # Terms
            terms_bool = True if terms == "on" else False

            #   Create User
            user.objects.create(
                name = fullName,
                email = email,
                password = hashed_password,
                terms = terms_bool
            )
            print(f'User is created with {email}')

            return render(request, 'public/login.html')
        except ValidationError as e:
            print("ERRORS:", e.message_dict)
            return render(request, 'public/signup.html',{
                 "errors": e.message_dict,
                 "input": {
                    "fullName": fullName,
                    "email": email,
                }
            })


    return render(request, 'public/signup.html')
