from .models import CustomUser
from rest_framework import generics, status
from rest_framework.response import Response

# Create your views here.

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializers import RegisterSerializer, LoginSerializer

from rest_framework.decorators import api_view
from django.shortcuts import render  # 이 부분을 추가해야 render 함수를 사용할 수 있습니다.


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def get(self, request, *args, **kwargs):
        return render(request, "users/register.html")  # 회원가입 페이지를 보여줌

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class LoginView(generics.GenericAPIView):
    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK)


@api_view(["POST"])
def logout_view(request):
    if request.auth:
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
