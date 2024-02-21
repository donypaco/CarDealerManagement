from rest_framework import generics
from .models import Car, Customer, Brand, Dealership, Purchase
from .serializers import CarSerializer, CustomerSerializer, BrandSerializer, DealershipSerializer, PurchaseSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class CarList(generics.ListCreateAPIView):
    serializer_class = CarSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['model', 'brand__name']
    ordering_fields = ['id']
    filterset_fields = ['model','brand__name'] 

    def get_queryset(self):
        queryset = Car.objects.all()
        brand_name = self.request.query_params.get('brand')
        model_name = self.request.query_params.get('model')
        if brand_name is not None:
            queryset = queryset.filter(brand__name=brand_name)
        if model_name is not None: 
            queryset = queryset.filter(model=model_name)

        return queryset

class CarDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    
class CustomerList(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'surname', 'email']
    ordering_fields = ['id']
    filterset_fields = ['name', 'surname', 'email'] 
    queryset = Customer.objects.all()
    
    
class CustomerDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class BrandList(generics.ListCreateAPIView):
    serializer_class = BrandSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name']
    ordering_fields = ['id']
    filterset_fields = ['name'] 
    queryset = Brand.objects.all()
    
class BrandDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    
class DealershipList(generics.ListCreateAPIView):
    serializer_class = DealershipSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name']
    ordering_fields = ['id']
    filterset_fields = ['name'] 

    queryset = Dealership.objects.all()
    
class DealershipDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DealershipSerializer
    queryset = Dealership.objects.all()

class PurchaseList(generics.ListCreateAPIView):
    serializer_class = PurchaseSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name']
    ordering_fields = ['id']
    filterset_fields = ['status'] 
    queryset = Purchase.objects.all()
    
class PurchaseDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()
