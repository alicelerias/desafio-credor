from django.urls import path
from .views import CustomerProposalView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('proposal/', CustomerProposalView.as_view(), name='customer_proposal'),
    # ...
]
