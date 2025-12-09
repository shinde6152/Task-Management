import re
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

def validate_signup_data(fullName, email, password, confirmPassword, terms):
    errors = {}

    # ----- Full Name -----
    if not fullName.strip():
        errors['fullName'] = "Full name cannot be empty."

    # ----- Email -----
    if not email:
        errors['email'] = "Email is required."
    elif '@' not in email:
        errors['email'] = "Invalid email format."
    elif User.objects.filter(email__iexact=email).exists():
        errors['email'] = "Email already exists."

    # ----- Password validation -----
    if len(password) < 8 or len(password) > 30:
        errors['password'] = "Password must be 8–15 characters long."
    elif " " in password:
        errors['password'] = "Password cannot contain spaces."
    elif not re.search(r"[A-Z]", password):
        errors['password'] = "Must include at least one uppercase letter."
    elif not re.search(r"[a-z]", password):
        errors['password'] = "Must include at least one lowercase letter."
    elif not re.search(r"\d", password):
        errors['password'] = "Must include at least one number."
    elif not re.search(r"[^\w\s]", password):
        errors['password'] = "Must include at least one special character."

    # ----- Confirm password -----
    if password != confirmPassword:
        errors['confirmPassword'] = "Passwords do not match."

    # ----- Terms -----
    if terms != "on":
        errors['terms'] = "You must accept Terms and Conditions."

    if errors:
        raise ValidationError(errors)