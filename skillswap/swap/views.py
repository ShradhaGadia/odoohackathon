from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer

class UserProfileAPI(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    def get_object(self):
        return self.request.user

from rest_framework import filters
from rest_framework import generics
from .models import Skill
from .serializers import SkillSerializer

class SkillSearchAPI(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import SwapRequest
from .serializers import SwapRequestSerializer

class SwapRequestListCreateAPI(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SwapRequestSerializer

    def get_queryset(self):
        return SwapRequest.objects.filter(from_user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)
