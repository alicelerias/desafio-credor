from rest_framework.generics import ListAPIView

from ..models import ProposalField
from ..serializers import ProposalFieldsSerializer


class ListProposalFields(ListAPIView):
    queryset = ProposalField.objects.order_by("order").all()
    serializer_class = ProposalFieldsSerializer
