# app/models.py

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    train = models.CharField(max_length=100)  # Example field, modify as per your requirements
    class_type = models.CharField(max_length=20)
    journey_date = models.DateField()
    from_place = models.CharField(max_length=100)
    to_place = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.train}"
