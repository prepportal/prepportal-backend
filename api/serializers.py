# serializers.py
from rest_framework import serializers

from .models import (Branch, Note, QuestionPaper, Semester, SemesterGroup,
                     Subject, SubjectType)


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class SemesterGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemesterGroup
        fields = '__all__'

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'

class SubjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectType
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class QuestionPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionPaper
        fields = '__all__'
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'