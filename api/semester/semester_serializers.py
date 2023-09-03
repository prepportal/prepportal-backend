from rest_framework import serializers
from ..models import Semester


class SemsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = "__all__"
