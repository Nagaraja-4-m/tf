from django.db import models

# Create your models here.

class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    email=models.EmailField(unique=True)
    fullname=models.CharField(max_length=256)
    password=models.CharField(max_length=64)
    status=models.SmallIntegerField(default=1)
    created_at=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='admins'
        