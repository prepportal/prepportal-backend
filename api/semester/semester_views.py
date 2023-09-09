from rest_framework.views import APIView
from api.models import Semester
from api.semester.semester_serializers import SemsterSerializer
from util.response import CustomResponse
from rest_framework import status


class SemesterAPI(APIView):
    def get(self, request, semester_id=None):
        try:
            if semester_id:
                semesters = Semester.objects.filter(semester_id=semester_id)
                if not semesters:
                    return CustomResponse(
                        general_message="Semester Does Not Exists"
                    ).get_failure_response(
                        status_code=status.HTTP_404_NOT_FOUND,
                        http_status_code=status.HTTP_404_NOT_FOUND,
                    )
            else:
                semesters = Semester.objects.all()
            serializer = SemsterSerializer(semesters, many=True)
            return CustomResponse(response=serializer.data).get_success_response()
        except Exception as e:
            return CustomResponse(message=e.messages).get_failure_response()
