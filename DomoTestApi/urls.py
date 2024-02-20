from django.urls import path
from DomoTestApi.serializers import CarSerializer
from .views import CustomerList, CustomerDetails, BrandList, BrandDetails, CarList, CarDetails, DealershipList, DealershipDetails

urlpatterns = [
    path('customer/', CustomerList.as_view()),
    path('customer/<int:pk>/', CustomerDetails.as_view()),
    path('brand/', BrandList.as_view()),
    path('brand/<int:pk>/', BrandDetails.as_view()),
    path('car/', CarList.as_view()),
    path('car/<int:pk>/', CarDetails.as_view()),
    path('dealership/', DealershipList.as_view()),
    path('dealership/<int:pk>/', DealershipDetails.as_view()),
]