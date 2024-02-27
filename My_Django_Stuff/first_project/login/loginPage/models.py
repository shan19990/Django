from django.db import models

# Create your models here.

class loginCredential(models.Model):
    userId = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)

    def __str__(self):
        return self.userId

class AccountDetails(models.Model):
    userId = models.ForeignKey(loginCredential,on_delete=models.CASCADE)
    name = models.CharField(max_length = 20)
    age = models.IntegerField(max_length=2)
    dob = models.CharField(max_length=20)