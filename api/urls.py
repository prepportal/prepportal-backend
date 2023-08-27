import debug_toolbar
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BranchViewSet, SemesterGroupViewSet, SemesterViewSet, SubjectTypeViewSet
# app_name will help us do a reverse look-up latter.
router = DefaultRouter()
router.register(r'branches', BranchViewSet)
router.register(r'semester-groups', SemesterGroupViewSet)
router.register(r'semesters', SemesterViewSet)
router.register(r'subject-types', SubjectTypeViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path("__debug__/", include(debug_toolbar.urls)),
]