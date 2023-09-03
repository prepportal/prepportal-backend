from django.urls import include, path
from api.note.note_views import NoteAPI


urlpatterns = [
    path("", NoteAPI.as_view()),
    path("<str:subject_id>/", NoteAPI.as_view()),
]
