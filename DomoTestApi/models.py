from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f"{self.name} {self.surname}"

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    model = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.brand} {self.model}"

class Dealership(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name