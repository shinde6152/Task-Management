from django.shortcuts import render, redirect
from ...validations.signupvalidation import validate_signup_data
from ...models.user import user
from django.contrib.auth.hashers import check_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password


def login(request):

    if request.method == "POST":

        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()

        errors = {}

        if not email:
            errors["email"] = "Email is required."

        if not password:
            errors["password"] = "Password is required."

        if errors:
            return render(request, "public/login.html", {
                "errors": errors,
                "input": {"email": email}
            })

        try:
            validate_email(email)
        except ValidationError:
            errors["email"] = "Invalid email format."
            return render(request, "public/login.html", {
                "errors": errors,
                "input": {"email": email}
            })

        try:
            user_obj = user.objects.get(email=email)
        except user.DoesNotExist:
            errors["email"] = "No account found for this email."
            return render(request, "public/login.html", {
                "errors": errors,
                "input": {"email": email}
            })

        if not user_obj.is_active:
            errors["account"] = "Your account is inactive. Contact admin."
            return render(request, "public/login.html", {
                "errors": errors,
                "input": {"email": email}
            })

        if not check_password(password, user_obj.password):
            errors["password"] = "Incorrect password."
            return render(request, "public/login.html", {
                "errors": errors,
                "input": {"email": email}
            })

        request.session["user_id"] = user_obj.id
        request.session["user_role"] = user_obj.role
        request.session["user_name"] = user_obj.name

        # Redirect based on role
        role = user_obj.role

        if role == "administrator":
            return redirect("administrator_dashboard")
        if role == "admin":
            return redirect("admin_dashboard")
        if role == "manager":
            return redirect("manager_dashboard")

        return redirect("user_dashboard")

    return render(request, "public/login.html")


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


def logout(request):
    # Clear entire session safely
    request.session.flush()

    # Redirect to login page
    return redirect("login")