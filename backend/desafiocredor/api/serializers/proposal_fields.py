from rest_framework import serializers

from ..models import ProposalField


class ProposalFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProposalField
        fields = ("name", "type", "nullable", "order")
