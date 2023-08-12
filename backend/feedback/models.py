from django.db import models
from users.models import CustomUser

# 사용자와 업로드한 비디오 연결
class UserUpload(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # key 필드 customuser 모델로 변경
    video = models.FileField(upload_to='uploaded_videos/')
    
    
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
    