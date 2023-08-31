from rest_framework import serializers
from ..models import SubjectType

class SubjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectType
        fields = '__all__'