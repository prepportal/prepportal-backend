from django.urls import include, path
from api.semester_group.semester_group_views import SemesterGroupAPI


urlpatterns = [
    path("", SemesterGroupAPI.as_view()),
    path("<str:semester_group_id>/", SemesterGroupAPI.as_view()),
]