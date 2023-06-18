from rest_framework.generics import ListAPIView

from ..models import ProposalFields
from ..serializers import ProposalFieldsSerializer


class ListProposalFields(ListAPIView):
    queryset = ProposalFields.objects.order_by("order").all()
    serializer_class = ProposalFieldsSerializer
