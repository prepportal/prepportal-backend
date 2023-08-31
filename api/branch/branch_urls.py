from django.urls import include, path
from api.branch.branch_views import BranchAPI


urlpatterns = [
    path("", BranchAPI.as_view()),
    path("<str:branch_id>/", BranchAPI.as_view()),
]