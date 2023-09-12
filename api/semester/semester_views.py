from rest_framework.views import APIView
from api.models import Semester
from api.semester.semester_serializers import SemsterSerializer
from util.response import CustomResponse
from rest_framework import status


class SemesterAPI(APIView):
    def get(self, request, branch_id=None):
        try:
            if branch_id:
                semesters = Semester.objects.filter(branch=branch_id)
                if not semesters:
                    return CustomResponse(
                        message="Semester Does Not Exists"
                    ).get_failure_response(
                        status_code=status.HTTP_404_NOT_FOUND,
                        http_status_code=status.HTTP_404_NOT_FOUND,
                    )
            else:
                semesters = Semester.objects.all().order_by('code')
            serializer = SemsterSerializer(semesters, many=True)
            return CustomResponse(response=serializer.data).get_success_response()
        except Exception as e:
            return CustomResponse(message=str(e)).get_failure_response()

    def patch(self, request, branch_id):
        try:
            semester = Semester.objects.get(semester_id=branch_id)
            serializer = SemsterSerializer(
                semester, data=request.data, partial=True
            )

            if serializer.is_valid():
                serializer.save()
                return CustomResponse(
                    response=serializer.data
                ).get_success_response()

            return CustomResponse(
                message=serializer.errors
            ).get_failure_response()
        except Exception as e:
            return CustomResponse(message=str(e)).get_failure_response()
