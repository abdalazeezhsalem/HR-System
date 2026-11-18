from rest_framework import serializers
from ..models import InterviewQuestionSet


class InterviewQuestionSetSerializer(serializers.ModelSerializer):
    candidate = serializers.StringRelatedField(read_only=True)
    job_position = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = InterviewQuestionSet
        field = '__all__'
