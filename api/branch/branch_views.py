from rest_framework.views import APIView
from api.models import Branch
from api.branch.branch_serializers import BranchSerializer
from util.response import CustomResponse
from rest_framework import status


class BranchAPI(APIView):
    def get(self, request, branch_id=None):
        try:
            if branch_id:
                branches = Branch.objects.filter(id=branch_id)
                if not branches:
                    return CustomResponse(
                        message="Branch Does Not Exists"
                    ).get_failure_response(status_code=status.HTTP_404_NOT_FOUND)
            else:
                branches = Branch.objects.all()
            serializer = BranchSerializer(branches, many=True)
            return CustomResponse(response=serializer.data).get_success_response()
        except Exception as e:
            return CustomResponse(message=str(e)).get_failure_response()
