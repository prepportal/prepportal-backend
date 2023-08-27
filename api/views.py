from rest_framework import viewsets

from .models import (Branch, Note, QuestionPaper, Semester, SemesterGroup,
                     Subject, SubjectType)
from .serializers import (BranchSerializer, NoteSerializer,
                          QuestionPaperSerializer, SemesterGroupSerializer,
                          SemesterSerializer, SubjectSerializer,
                          SubjectTypeSerializer)


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

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class QuestionPaperViewSet(viewsets.ModelViewSet):
    queryset = QuestionPaper.objects.all()
    serializer_class = QuestionPaperSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer