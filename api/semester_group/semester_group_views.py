from rest_framework.views import APIView
from api.models import SemesterGroup
from api.semester_group.semester_group_serializers import SemsterGroupSerializer
from util.response import CustomResponse
from rest_framework import status


class SemesterGroupAPI(APIView):
    def get(self, request, semester_group_id=None):
        try:
            if semester_group_id:
                groups = SemesterGroup.objects.filter(
                    semester_group_id=semester_group_id
                )
                if not groups:
                    return CustomResponse(
                        general_message="Semester Group Does Not Exists"
                    ).get_failure_response(
                        status_code=status.HTTP_404_NOT_FOUND,
                        http_status_code=status.HTTP_404_NOT_FOUND,
                    )
            else:
                groups = SemesterGroup.objects.all()
            serializer = SemsterGroupSerializer(groups, many=True)
            return CustomResponse(response=serializer.data).get_success_response()
        except Exception as e:
            return CustomResponse(general_message=str(e)).get_failure_response()
