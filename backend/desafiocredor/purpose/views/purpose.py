from rest_framework import viewsets

from ..models import Purpose
from ..serializers import PurposeSerializer

class PurposeViewSet(viewsets.ModelViewSet):
    queryset = Purpose.objects.all()
    serializer_class = PurposeSerializer
