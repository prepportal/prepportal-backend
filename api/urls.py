import debug_toolbar
from django.urls import include, path


urlpatterns = [
    path("branches/", include('api.branch.branch_urls')),
    path("semesters/", include("api.semester.semester_urls")),
    path("subject-types/", include("api.subject_type.subject_type_urls")),
    path("subjects/", include("api.subject.subject_urls")),
    path("question-papers/", include("api.question_paper.question_paper_urls")),
    path("notes/", include("api.note.note_urls")),
    path('user/', include('rest_registration.api.urls')),


    path("__debug__/", include(debug_toolbar.urls)),
]