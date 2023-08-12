from rest_framework import serializers
from .models import UserUpload

class UserUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserUpload
        fields = '__all__'   # 모든 필드 포함
        