from django.db import models


class User(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    login = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.login


class UsersEntries(models.Model):
    entry = models.ForeignKey(User, on_delete=models.CASCADE)
    currentip = models.CharField(max_length=16)
    data_time = models.DateTimeField(auto_now=True)
