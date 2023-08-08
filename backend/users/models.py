from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):       #일반 사용자 생성 메서드
    def create_user(self, username, nickname, email, password=None, **extra_fields):
        if not email:
            raise ValueError("이메일 써 ㅣ놈아")
        email = self.normalize_email(email)
        user = self.model(username=username, nickname=nickname, email=email, **extra_fields)      # **extra_fields 추가적인 키워드 인자 딕셔너리 형태로 받을게
        user.set_password(password)
        user.save(using=self._db)       #사용자 DB에 저장
        return user
    
    def create_superuser(self, username, nickname, email, password=None,**extra_fields):
        extra_fields.setdefault('is_staff', True)       #관리자 권한 부여
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(username, nickname, email, password, **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    nickname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name="customuser_set",
        related_query_name="customuser",
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name="customuser_set",
        related_query_name="customuser",
    )
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nickname', 'email']

    def __str__(self):
        return str(self.user_id)


