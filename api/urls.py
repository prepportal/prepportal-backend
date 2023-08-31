import debug_toolbar
from django.urls import include, path


urlpatterns = [
    path("branches/", include('api.branch.branch_urls')),
    path("semester-groups/", include("api.semester_group.semester_group_urls")),
    path("semesters/", include("api.semester.semester_urls")),
    path("__debug__/", include(debug_toolbar.urls)),
]