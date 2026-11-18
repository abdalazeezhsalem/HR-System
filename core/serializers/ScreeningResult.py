from rest_framework import serializers

from ..models import ScreeningResult

class ScreeningResultSerializer(serializers.ModelSerializer):
    candidate = serializers.StringRelatedField(read_only=True)
    job_position = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ScreeningResult
        fields ='__all__'
