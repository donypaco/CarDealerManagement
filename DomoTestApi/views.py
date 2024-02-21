from rest_framework import generics, status
from .models import Car, Customer, Brand, Dealership, Purchase
from .serializers import CarSerializer, CustomerSerializer, BrandSerializer, DealershipSerializer, PurchaseSerializer, UserSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate

class UserSignup(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class CarList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    
class CustomerList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'surname', 'email']
    ordering_fields = ['id']
    filterset_fields = ['name', 'surname', 'email'] 
    queryset = Customer.objects.all()
    
    
class CustomerDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class BrandList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BrandSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name']
    ordering_fields = ['id']
    filterset_fields = ['name'] 
    queryset = Brand.objects.all()
    
class BrandDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    
class DealershipList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DealershipSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name']
    ordering_fields = ['id']
    filterset_fields = ['name'] 

    queryset = Dealership.objects.all()
    
class DealershipDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DealershipSerializer
    queryset = Dealership.objects.all()

class PurchaseList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PurchaseSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name']
    ordering_fields = ['id']
    filterset_fields = ['status'] 
    queryset = Purchase.objects.all()
    
class PurchaseDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()
