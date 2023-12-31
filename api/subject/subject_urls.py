from django.urls import include, path
from api.subject.subject_views import SubjectAPI


urlpatterns = [
    path("", SubjectAPI.as_view()),
    path("<str:branch_id>/<str:semester_id>/", SubjectAPI.as_view()),
]
