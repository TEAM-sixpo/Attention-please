from django.db import models
from users.models import CustomUser
# Create your models here.

class UserUpload(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # key 필드 customuser 모델로 변경
    video = models.FileField(upload_to='uploaded_videos/')
    
    
    def __str__(self):
        return f"{self.user.username}"
