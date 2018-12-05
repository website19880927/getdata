from django.db import models

# Create your models here.

class User(models.Model):
    #设置用户名与密码
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    class Meta:
        db_table='t_user'

class Alu(models.Model):
    size = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    class Meta:
        db_table = 't_num'
