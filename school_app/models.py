from django.db import models

class User(models.Model):
    number = models.CharField(max_length=9)
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.id}: {self.name}, {self.number}"