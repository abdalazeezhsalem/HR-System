from rest_framework import serializers

from ..models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    candidate = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Resume
        fields = '__all__'
