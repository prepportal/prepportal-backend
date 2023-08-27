# serializers.py
from rest_framework import serializers
from .models import Branch, SemesterGroup, Semester, SubjectType

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