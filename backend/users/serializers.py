from django.contrib.auth.models import User     #User 모델
from django.contrib.auth.password_validation import validate_password       #Django 기본 패스워드 검증 도구

from rest_framework import serializers
from rest_framework.authtoken.models import Token       #Token 모델
from rest_framework.validators import UniqueValidator       # 이메일 중복 방지 위한 검증 도구

class RegisterSerializer(serializers.ModelSerializer):     # 회원가입 시리얼라이저
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())],        # 이메일 중복검증
    )
    
    class Meta:
        model = User
        fields = ('username', 'password', 'email')