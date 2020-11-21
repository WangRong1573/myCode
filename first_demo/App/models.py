from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=128)

    class Meta:
        # 指定表名
        db_table = 'user'