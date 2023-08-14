from django.db import models


class Vehicle(models.Model):
    TYPE_CHOICES = [
        ('Two-Wheeler', 'Two-Wheeler'),
        ('Three-Wheeler', 'Three-Wheeler'),
        ('Four-Wheeler', 'Four-Wheeler'),
    ]

    number = models.CharField(max_length=150)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    model = models.TextField(max_length=300, default=" ")
    description = models.TextField(max_length=300, default=" ")

    def __str__(self):
        return self.number