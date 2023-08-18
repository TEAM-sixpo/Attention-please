import os
from uuid import uuid4
from django.utils import timezone
from django.db import models
from users.models import CustomUser



# 파일명 동적으로 생성
def name_path(instance, filename):
    upload_to = 'uploaded_videos/'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)

# 사용자와 업로드한 비디오 연결
class UserUpload(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # key 필드 customuser 모델로 변경
    video = models.FileField(upload_to=name_path)     # FileField 하면 모델에 저장ㄴㄴ 경로만 저장
    script = models.TextField(blank=True, null=True)    # 사용자 스크립트 입력
    
    def __str__(self):
        return f"{self.user.username}"

# UserUpload 모델에 1대1로 연결, 영상에 대한 정보는 하나만 존재해야 한다는 의미
class Video(models.Model):
    user_upload = models.OneToOneField(UserUpload, on_delete=models.CASCADE, related_name='video_detail')
    videoname = models.CharField(max_length=255)
    videouploaddate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.videoname 
    
    
#Video 모델에 ForeignKey 로 연결, 한 비디오에 여러 개 피드백 존재가능
class Feedback(models.Model):
    Video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='feedbacks')
    speed = models.IntegerField()
    accuracy = models.DecimalField(max_digits=5, decimal_places=2)      # max_digits 는 숫자 최대 자릿수, places 는 소수점 자릿수
    intensity = models.IntegerField()
    posture = models.CharField(max_length=255)      # 자세에 대한 문자열 피드백 담는 필드
    
