from rest_framework import serializers
from ..models import ProposalFields


class ProposalFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProposalFields
        fields = ("name", "type", "nullable", "order")
