from django.contrib import admin
from .models import Car, Customer, Brand, Dealership, Purchase

admin.site.register(Car)
admin.site.register(Customer)
admin.site.register(Brand)
admin.site.register(Dealership)
admin.site.register(Purchase)
