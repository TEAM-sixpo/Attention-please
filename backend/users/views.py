from django.contrib.auth.models import User
from rest_framework import generics
# Create your views here.

from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer