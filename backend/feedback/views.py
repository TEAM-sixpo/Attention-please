from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import UserUpload
from .serializer import UserUploadSerializer

class UserUploadViewSet(viewsets.ModelViewSet):
    queryset = UserUpload.objects.all()
    serializer_class = UserUploadSerializer
    # permission_classes = [IsAuthenticated]  # 이 뷰에 대한 접근권한, 로그인 사용자만 뷰 사용가능
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        # 영상 업로드 처리할 때 호출되는 메서드, 영상에 사용자 정보 추가