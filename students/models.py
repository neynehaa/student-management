from django.db import models

class Student(models.Model): 
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
