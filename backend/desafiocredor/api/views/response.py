from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..serializers import ResponseSerializer, ProposalSerializer
from ..tasks import process_proposal

from django.db import transaction


@api_view(["POST"])
def create_proposal(request):
    with transaction.atomic():
        proposal_data = {"status": "pending"}
        proposal_serializer = ProposalSerializer(data=proposal_data)
        if not proposal_serializer.is_valid():
            return Response(
                proposal_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        proposal = proposal_serializer.save()
        response_data = request.data.get("responses", [])
        for response in response_data:
            response["proposal"] = proposal.id

        response_serializer = ResponseSerializer(data=response_data, many=True)

        if not response_serializer.is_valid():
            transaction.set_rollback(True)
            return Response(
                response_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        response_serializer.save()
        response_data = {
            "proposal": proposal_serializer.data,
            "responses": response_serializer.data,
        }

        # send proposal to queue
        process_proposal.delay(proposal.id)

    return Response(response_data, status=status.HTTP_201_CREATED)
