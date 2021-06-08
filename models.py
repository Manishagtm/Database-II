from django.db import models


class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "login"


class Sign(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=16)
    password1 = models.CharField(max_length=16)

    def __str__(self):
        return self.Name

    class Meta:
        db_table = "sign"
