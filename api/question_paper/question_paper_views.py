from rest_framework.views import APIView
from api.models import QuestionPaper
from api.question_paper.question_paper_serializers import QuestionPaperSerializer
from util.response import CustomResponse
from util.pagination import get_paginated_queryset
from rest_framework import status


class QuestionPaperAPI(APIView):
    def get(self, request, subject_id=None):
        try:
            if subject_id:
                if not (
                    question_papers := QuestionPaper.objects.filter(
                        id=subject_id
                    )
                ):
                    return CustomResponse(
                        message="Question Paper Does Not Exists"
                    ).get_failure_response(
                        status_code=status.HTTP_404_NOT_FOUND,
                        http_status_code=status.HTTP_404_NOT_FOUND,
                    )
                serializer = QuestionPaperSerializer(question_papers, many=True)
                return CustomResponse(response=serializer.data).get_success_response()
            else:
                question_papers = QuestionPaper.objects.all()
                paginated_queryset = get_paginated_queryset(
                    question_papers, request, ["name"], {"name": "name"}
                )
                serializer = QuestionPaperSerializer(
                    paginated_queryset.get("queryset"), many=True
                )
                return CustomResponse().paginated_response(
                    data=serializer.data,
                    pagination=paginated_queryset.get("pagination"),
                )
        except Exception as e:
            return CustomResponse(message=str(e)).get_failure_response()

    def post(self, request):
        pass
