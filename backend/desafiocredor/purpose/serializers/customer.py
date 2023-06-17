from rest_framework import serializers
from ..models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150)
    cpf = serializers.IntegerField()
    adress = serializers.CharField(max_length=200)

    def validate_name(self, name: str) -> str:
        if not name:
            raise serializers.ValidationError("Insert a valid name")
        return name
    
    def validate_cpf(self, cpf: int) -> int:
        if not cpf:
            raise serializers.ValidationError("Insert a valid cpf")
        if len(str(cpf)) != 11:
            raise serializers.ValidationError("Cpf must be 11 digits")
        return cpf
    
    def validate_adress(self, adress: str) -> str:
        if not adress:
            raise serializers.ValidationError("Insert a valid adress")
        return adress

    def create(self, validated_data) -> Customer:
        return Customer.objects.create(**validated_data)

    class Meta:
        model = Customer
        fields = ['id', 'name', 'cpf', 'adress']
