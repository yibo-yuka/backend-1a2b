from django.db import models

class UserScore(models.Model):
    # 使用者名稱：使用 CharField，max_length 是必填參數
    username = models.CharField(max_length=100, unique=True, verbose_name="username")
    
    # 分數：使用 IntegerField，預設值設為 0
    score = models.IntegerField(default=0, verbose_name="score")

    # 建立時間與更新時間（建議加上，方便後續管理資料）
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # 設定資料表在資料庫中的名稱（可選）
        db_table = 'user_scores'
        # 設定後台顯示的名稱
        verbose_name = "User Score"
        verbose_name_plural = "User Scores"

    def __str__(self):
        # 讓 Django Admin 或終端機顯示時更易讀
        return f"{self.username}: {self.score}"