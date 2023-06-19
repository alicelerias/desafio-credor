from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..serializers import ResponseSerializer, ProposalSerializer

@api_view(['POST'])
def create_proposal(request):
    proposal_data = {'status': 'pending'}
    proposal_serializer = ProposalSerializer(data=proposal_data)
    if proposal_serializer.is_valid():
        proposal = proposal_serializer.save()
        response_data = request.data.get('responses', [])
        for response in response_data:
            response["proposal"] = proposal.id

        response_serializer = ResponseSerializer(data=response_data, many=True)
        if response_serializer.is_valid():
            response_serializer.save()
            response_data = {
                'proposal': proposal_serializer.data,
                'responses': response_serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            proposal.delete()
            return Response(response_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else: 
        return Response(proposal_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
