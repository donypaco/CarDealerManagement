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
    phone = models.CharField(max_length=20, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    PENDING = 'pending'
    COMPLETED = 'completed'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return f"{self.customer.name} - {self.car} - ${self.price}"
