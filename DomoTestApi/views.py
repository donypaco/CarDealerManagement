from rest_framework import generics
from .models import Car, Customer, Brand, Dealership
from .serializers import CarSerializer, CustomerSerializer, BrandSerializer, DealershipSerializer


class CarList(generics.ListCreateAPIView):
    serializer_class = CarSerializer
    def get_queryset(self):
        queryset = Car.objects.all()
        brand = self.request.query_params.get('brand')
        if brand is not None:
            queryset = queryset.filter(brand = brand)
        return queryset
    
class CarDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    
class CustomerList(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    
class CustomerDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class BrandList(generics.ListCreateAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    
class BrandDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    
class DealershipList(generics.ListCreateAPIView):
    serializer_class = DealershipSerializer
    queryset = Dealership.objects.all()
    
class DealershipDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DealershipSerializer
    queryset = Dealership.objects.all()
