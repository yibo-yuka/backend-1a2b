from django.urls import path
from .views import UserScoreListCreateView, handle_score

urlpatterns = [
    # GET: 用於取得排行榜 (由 generics 提供)
    path('scores/', UserScoreListCreateView.as_view(), name='score-list'),
    
    # POST: 用於更新或登記分數 (由你寫的 handle_score 函式提供)
    # 建議路徑稍作區分，方便管理
    path('scores/update/', handle_score, name='score-update'),
]