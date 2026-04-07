from rest_framework import generics
from .models import UserScore
from .serializers import UserScoreSerializer

class UserScoreListCreateView(generics.ListCreateAPIView):
    queryset = UserScore.objects.all().order_by('-score') # 依分數高低排序
    serializer_class = UserScoreSerializer