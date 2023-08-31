from django.urls import include, path
from api.subject_type.subject_type_views import SubjectTypeAPI


urlpatterns = [
    path("", SubjectTypeAPI.as_view()),
    path("<str:subject_type_id>/", SubjectTypeAPI.as_view()),
]