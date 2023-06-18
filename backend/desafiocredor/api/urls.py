from django.urls import path
from .views import ListProposalFields

urlpatterns = [
    path(
        "proposal/fields/", ListProposalFields.as_view(), name="proposal_fields"
    ),
]
