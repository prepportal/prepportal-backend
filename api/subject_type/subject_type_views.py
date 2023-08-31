from rest_framework.views import APIView
from api.models import SubjectType
from api.subject_type.subject_type_serializers import SubjectTypeSerializer
from util.response import CustomResponse
from rest_framework import status


class SubjectTypeAPI(APIView):
    def get(self, request, subject_type_id=None):
        try:
            if subject_type_id:
                subject_types = SubjectType.objects.filter(
                    subject_type_id=subject_type_id
                )
                if not subject_types:
                    return CustomResponse(
                        general_message="Semester Type Does Not Exists"
                    ).get_failure_response(
                        status_code=status.HTTP_404_NOT_FOUND,
                        http_status_code=status.HTTP_404_NOT_FOUND,
                    )
            else:
                subject_types = SubjectType.objects.all()
            serializer = SubjectTypeSerializer(subject_types, many=True)
            return CustomResponse(response=serializer.data).get_success_response()
        except Exception as e:
            return CustomResponse(general_message=str(e)).get_failure_response()
