from rest_framework import viewsets

from .models import Branch, Semester, SemesterGroup, SubjectType
from .serializers import (BranchSerializer, SemesterGroupSerializer,
                          SemesterSerializer, SubjectTypeSerializer)


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class SemesterGroupViewSet(viewsets.ModelViewSet):
    queryset = SemesterGroup.objects.all()
    serializer_class = SemesterGroupSerializer

class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer

class SubjectTypeViewSet(viewsets.ModelViewSet):
    queryset = SubjectType.objects.all()
    serializer_class = SubjectTypeSerializer