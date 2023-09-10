from django.urls import include, path
from api.semester.semester_views import SemesterAPI


urlpatterns = [
    path("", SemesterAPI.as_view()),
    path("<str:branch_id>/", SemesterAPI.as_view()),
]
