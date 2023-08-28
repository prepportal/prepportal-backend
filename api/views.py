from rest_framework import viewsets, status
from rest_framework.response import Response

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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        code = serializer.validated_data['code']
        if Subject.objects.filter(code=code).first():
            return Response({"detail": "Subject already exists."}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        if code := self.request.query_params.get('code'):
            return Subject.objects.filter(code=code)
        return Subject.objects.all()
    
class QuestionPaperViewSet(viewsets.ModelViewSet):
    queryset = QuestionPaper.objects.all()
    serializer_class = QuestionPaperSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer