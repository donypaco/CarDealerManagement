from rest_framework import serializers
from .models import Car, Customer, Brand, Dealership, Purchase

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('__all__')

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('__all__')
        
class CarSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name')

    class Meta:
        model = Car
        fields = ('id','model', 'brand_name')

    def create(self, validated_data):
        brand_data = validated_data.pop('brand', None)
        if brand_data:
            brand_name = brand_data.get('name')
            existing_brand = Brand.objects.filter(name=brand_name).first()
            if existing_brand:
                validated_data['brand'] = existing_brand
            else:
                validated_data['brand'] = Brand.objects.create(name=brand_name)
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        brand_data = validated_data.pop('brand', None)
        if brand_data:
            brand_name = brand_data.get('name')
            existing_brand = Brand.objects.filter(name=brand_name).first()
            if existing_brand:
                validated_data['brand'] = existing_brand
            else:
                validated_data['brand'] = Brand.objects.create(name=brand_name)
        return super().update(instance, validated_data)
                    
class DealershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealership
        fields = ('__all__')
        
class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ('__all__')