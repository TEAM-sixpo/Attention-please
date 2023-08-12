from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserUploadViewSet

router = DefaultRouter()    # API의 URL 주소 자동 생성
router.register(r'uploads', UserUploadViewSet)      # 어떤 모델과 뷰셋 연결할지 알려주는 역할

urlpatterns = [
    path('', include(router.urls)),
]
