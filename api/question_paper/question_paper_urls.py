from django.urls import include, path
from api.question_paper.question_paper_views import QuestionPaperAPI


urlpatterns = [
    path("", QuestionPaperAPI.as_view()),
    path("<str:subject_id>/", QuestionPaperAPI.as_view()),
]