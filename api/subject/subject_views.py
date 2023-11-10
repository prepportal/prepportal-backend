from rest_framework.views import APIView
from api.models import Subject
from api.subject.subject_serializers import SubjectSerializer
from util.response import CustomResponse
from util.pagination import get_paginated_queryset
from rest_framework import status


class SubjectAPI(APIView):
    def get(self, request, semester_id=None):
        try:
            if semester_id:
                if not (subjects := Subject.objects.filter(semester_id=semester_id)):
                    return CustomResponse(
                        message="Subject Does Not Exists"
                    ).get_failure_response(
                        status_code=status.HTTP_404_NOT_FOUND,
                        http_status_code=status.HTTP_404_NOT_FOUND,
                    )
                serializer = SubjectSerializer(subjects, many=True)
                return CustomResponse(response=serializer.data).get_success_response()
            else:
                subjects = Subject.objects.all()
                paginated_queryset = get_paginated_queryset(
                    subjects, request, ["name"], {"name": "name"}
                )
                serializer = SubjectSerializer(
                    paginated_queryset.get("queryset"), many=True
                )
                return CustomResponse().paginated_response(
                    data=serializer.data,
                    pagination=paginated_queryset.get("pagination"),
                )
        except Exception as e:
            return CustomResponse(message=str(e)).get_failure_response()
