from users.models import CustomUser     #CustomUser 모델
from django.contrib.auth.password_validation import validate_password       #Django 기본 패스워드 검증 도구
from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.authtoken.models import Token       #Token 모델
from rest_framework.validators import UniqueValidator       # 이메일 중복 방지 위한 검증 도구

class RegisterSerializer(serializers.ModelSerializer):     # 회원가입 시리얼라이저
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=CustomUser.objects.all())],        # 이메일 중복검증
    )
    password = serializers.CharField(write_only=True, required=True)
    # required=True 회원가입 시 비번 반드시 입력
    # write_only=True 데이터 응답 반환할때 password 포함안함
    
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'nickname', 'email')
        
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            nickname=validated_data['nickname'],
            email=validated_data['email']
        )
        return user
        
        
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    
    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError(
            {"error": "Unable to log in with provided credentials."}
        )