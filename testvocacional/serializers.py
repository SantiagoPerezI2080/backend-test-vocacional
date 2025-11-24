from rest_framework import serializers
from .models import VocationalTestResult

class VocationalTestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = VocationalTestResult
        fields = '__all__'
