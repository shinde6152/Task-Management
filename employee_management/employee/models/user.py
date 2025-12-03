from django.db import models

class user(models.Model):

    ROLE_CHOICES = (
        ("administrator", "Administrator"),
        ("admin", "Admin"),
        ("manager", "Manager"),
        ("user", "User"),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)  # will store hashed password
    terms = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="user")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.role})"