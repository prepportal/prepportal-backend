from rest_framework.views import APIView
from api.models import Note
from api.note.note_serializers import NoteSerializer
from util.response import CustomResponse
from util.pagination import get_paginated_queryset
from rest_framework import status


class NoteAPI(APIView):
    def get(self, request, subject_id=None):
        try:
            if subject_id:
                if not (notes := Note.objects.filter(subject_id=subject_id)):
                    return CustomResponse(
                        general_message="Question Paper Does Not Exists"
                    ).get_failure_response(
                        status_code=status.HTTP_404_NOT_FOUND,
                        http_status_code=status.HTTP_404_NOT_FOUND,
                    )
                serializer = NoteSerializer(notes, many=True)
                return CustomResponse(response=serializer.data).get_success_response()
            else:
                question_papers = notes.objects.all()
                paginated_queryset = get_paginated_queryset(
                    question_papers, request, ["name"], {"name": "name"}
                )
                serializer = NoteSerializer(
                    paginated_queryset.get("queryset"), many=True
                )
                return CustomResponse().paginated_response(
                    data=serializer.data,
                    pagination=paginated_queryset.get("pagination"),
                )
        except Exception as e:
            return CustomResponse(general_message=str(e)).get_failure_response()
