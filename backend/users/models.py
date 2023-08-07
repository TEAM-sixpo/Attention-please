from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):       #일반 사용자 생성 메서드
    def create_user(self, user_id, nickname, email, password=None, **extra_fields):
        if not email:
            raise ValueError("이메일 써 ㅣ놈아")
        email = self.normalize_email(email)
        user = self.model(user_id=user_id, nickname=nickname, email=email, **extra_fields)      # **extra_fields 추가적인 키워드 인자 딕셔너리 형태로 받을게
        user.set_password(password)
        user.save(using=self._db)       #사용자 DB에 저장
        return user
    
    def create_superuser(self, user_id, nickname, email, password=None):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(user_id, nickname, )