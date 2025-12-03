from django.db import models

class employee_data(models.Model):
    id = models.AutoField(primary_key=True)         #   Auto increment
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)        #   Current timestamp of record create
    last_update_at = models.DateTimeField(auto_now=True)        #   Last timestamp of record update
    is_active = models.BooleanField(default=True)               #   able to identify the record is deleted.


    def __str__(self):
        return self.name