from rest_framework import generics, status
from .models import UserScore
from .serializers import UserScoreSerializer
from django.db.models import F
from rest_framework.response import Response
from rest_framework.decorators import api_view

class UserScoreListCreateView(generics.ListAPIView):
    queryset = UserScore.objects.all().order_by('-score')[:20] # 依分數高低排序
    serializer_class = UserScoreSerializer
    
@api_view(['POST'])
def handle_score(request):
    name = request.data.get('username')
    
    # 基本驗證：確保有名字
    if not name or str(name).strip() == "":
        return Response({"error": "必須提供使用者名稱"}, status=status.HTTP_400_BAD_REQUEST)
    
    # 1. 取得或建立該使用者
    # defaults 代表如果是「新建」時要給予的初始值
    obj, created = UserScore.objects.get_or_create(username=name.strip(), defaults={'score': 0})
    
    # 2. 不論是新是舊，都將分數 +1
    # 使用 F() 表達式直接在資料庫層級做加法，避免 Race Condition
    obj.score = F('score') + 1
    obj.save()
    
    # 重新整理物件以取得運算後的數值（選用）
    obj.refresh_from_db()
    
    return Response({
        "message": "更新成功",
        "username": obj.username,
        "current_score": obj.score
    }, status=status.HTTP_200_OK)