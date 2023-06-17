from rest_framework import serializers
from ..models import Purpose
from .customer import CustomerSerializer

class PurposeSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    value = serializers.IntegerField()

    def validate_customer(self, customer: CustomerSerializer) -> CustomerSerializer:
        if not customer:
            raise serializers.ValidationError("Customer not to be null.")
        return customer

    def validate_value(self, value: int) -> int:
        if value <= 0:
            raise serializers.ValidationError("Value must be greater than zero.")
        return value
    
    def create(self, validated_data) -> Purpose:
        return Purpose.objects.create(**validated_data)
    
    class Meta:
        model = Purpose
        fields = ['id', 'customer', 'value', 'accepted', '-created_at']
        
