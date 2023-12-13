from django.db import models
from django.contrib.auth.models import User
# timezone 用於處理時間相關事務。
from django.utils import timezone
from django.urls import reverse
from PIL import Image


class ArticleColumn(models.Model):
    """
    分類的 Model
    """
    # 分類的標題
    title = models.CharField(max_length=100, blank=True)
    # 創建時間
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# Blog文章數據模型
class ArticlePost(models.Model):
    # 文章作者。參數 on_delete 用於指定數據刪除的方式，避免兩個關聯表的數據不一致
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 文章標題
    title = models.CharField(max_length=100)

    # 文章正文。保存大量文本使用 TextField
    body = models.TextField()

    # 文章創建時間。參數 default=timezone.now 指定其在創建數據時將默認寫入當前的時間
    created = models.DateTimeField(default=timezone.now)

    # 文章更新時間。參數 auto_now=True 指定每次數據更新時自動寫入當前時間
    updated = models.DateTimeField(auto_now=True)
    
    # 文章分類的 “一對多” 外鍵
    column = models.ForeignKey(
        ArticleColumn,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='article'
    )
    # 文章標題圖
    avatar = models.ImageField(upload_to='article/%Y%m%d/', blank=True)

    
    # 瀏覽數
    total_views = models.PositiveIntegerField(default=0)
    class Meta:
        # ordering 指定模型返回的數據的排列順序
    	# '-created' 表明數據應該以倒序排列
        ordering = ('-created',)
        
    def __str__(self):
        # 將文章標題返回
        return self.title
    
    # 獲取文章地址
    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])
    
    # 保存時處理圖片
    def save(self, *args, **kwargs):
        # 調用原有的 save() 的功能
        article = super(ArticlePost, self).save(*args, **kwargs)

        # 固定寬度縮放圖片大小
        if self.avatar and not kwargs.get('update_fields'):
            image = Image.open(self.avatar)
            (x, y) = image.size
            new_x = 400
            new_y = int(new_x * (y / x))
            resized_image = image.resize((new_x, new_y), Image.ANTIALIAS)
            resized_image.save(self.avatar.path)

        return article
    


    

   