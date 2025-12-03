from django.contrib import admin
from .models import employee_data
from .models.user import user
# Register your models here.

admin.site.register(employee_data)
admin.site.register(user)