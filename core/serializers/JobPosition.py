from rest_framework import serializers

from . import DepartmentSerializer
from ..models import JobPosition ,RequiredSkill


class RequiredSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequiredSkill
        fields = ['title']

class JobPositionSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    required_skills = RequiredSkillsSerializer(many=True, read_only=True)


    class Meta:
        model = JobPosition
        fields = '__all__'
