from rest_framework import serializers
from ..models import SemesterGroup


class SemsterGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemesterGroup
        fields = "__all__"
