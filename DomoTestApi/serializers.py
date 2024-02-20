from rest_framework import serializers
from .models import Car, Customer, Brand, Dealership

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('__all__')

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name')
        
class CarSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(required=False)

    class Meta:
        model = Car
        fields = ('model', 'brand')

    def create(self, validated_data):
        brand_data = validated_data.pop('brand', None)
        if brand_data:
            brand_name = brand_data.get('name')
            existing_brand = Brand.objects.filter(name=brand_name).first()
            if existing_brand:
                validated_data['brand'] = existing_brand
            else:
                # If brand doesn't exist, create a new one
                validated_data['brand'] = Brand.objects.create(name=brand_name)
        return super().create(validated_data)

    
        
class DealershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealership
        fields = ('__all__')