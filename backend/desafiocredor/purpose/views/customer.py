from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Customer, Proposal
from ..serializers import CustomerSerializer, ProposalSerializer

class CustomerProposalView(APIView):
    def analyse_proposal(self) -> bool:
        last_proposal = Proposal.objects.all()
        true = []
        false = []
        for item in last_proposal:
            if item.accepted == True:
                true.append(item)
            else:
                false.append(item)
        if len(false) >= len(true):
            return True
        else: return False

    
    def post(self, request):
        proposal = request.data
        proposal["accepted"] = self.analyse_proposal()
        customer_serializer = CustomerSerializer(data=request.data)
        proposal_serializer = ProposalSerializer(data=proposal)
        
        if customer_serializer.is_valid(raise_exception=True) and proposal_serializer.is_valid(raise_exception=True):
            customer = customer_serializer.save()
            proposal = proposal_serializer.save(customer=customer)

            response_data = {
                "customer": customer_serializer.data,
                "proposal": proposal_serializer.data
            }

            


            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        customers = Customer.objects.all()
        proposals = Proposal.objects.all()

        customer_serializer = CustomerSerializer(customers, many=True)
        proposal_serializer = ProposalSerializer(proposals, many=True)

        response_data = {
            "customers": customer_serializer.data,
            "proposals": proposal_serializer.data
        }

        return Response(response_data, status=status.HTTP_200_OK)

