from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import UserUpload, Video, Feedback
from .serializer import UserUploadSerializer, FeedbackSerializer


# 사용자 영상 분석, 딕셔너리 형태로 반환
def process_video(video):
    return


# 동영상 저장 및 관리
class UserUploadViewSet(viewsets.ModelViewSet):
    queryset = UserUpload.objects.all()
    serializer_class = UserUploadSerializer
    # permission_classes = [IsAuthenticated]  # 이 뷰에 대한 접근권한, 로그인 사용자만 뷰 사용가능
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        # UserUpload 모델에 저장된 후 Video 모델에도 정보 저장
        video_instance = Video.objects.create(
            user_upload=serializer.instance,
            videoname=str(serializer.instance.video)
        )
        
        # 영상, 자연어 처리 통한 피드백 생성
        processed_data = process_video(serializer.instance.video)
        
        # 처리된 데이터 기반 피드백 생성
        Feedback.objects.create(
            Video=video_instance,
            speed=processed_data['speed'],
            accuracy=processed_data.get('accuracy', 0),
            intensity=processed_data['intensity'],
            posture=processed_data.get('posture', 'Unknown')
        )
        
        
        
# 피드백 조회
class FeedbackListView(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    
def get_queryset(self):
    # 로그인한 사용자의 경우
    if self.request.user.is_authenticated:
        user = self.request.user
        return Feedback.objects.filter(Video__user_upload__user=user)

    # 로그인하지 않은 사용자의 경우
    return Feedback.objects.all()  # 모든 피드백 반환