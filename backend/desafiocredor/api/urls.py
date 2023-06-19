from django.urls import path
from .views import ListProposalFields, create_proposal

urlpatterns = [
    path("proposal/fields/", ListProposalFields.as_view(), name="proposal_fields"),
    path('proposals/', create_proposal, name='create-proposal'),
]
