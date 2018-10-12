from django.db import models

# Create your models here
class UserRegisterDetails(models.Model):
    user_name = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    def __str__(self):
        return self.name


##class Bookbed(models.Model):
    #name = models.CharField(max_length = 100)
