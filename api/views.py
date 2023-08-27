from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import viewsets
from .models import Branch, SemesterGroup, Semester
from .serializers import BranchSerializer, SemesterGroupSerializer, SemesterSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class SemesterGroupViewSet(viewsets.ModelViewSet):
    queryset = SemesterGroup.objects.all()
    serializer_class = SemesterGroupSerializer

class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer