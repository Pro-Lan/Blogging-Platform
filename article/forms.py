from django import forms
from .models import ArticlePost

# 寫文章的表單類
class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 指明數據模型來源
        model = ArticlePost
        # 定義表單包含的字段
        fields = ('title', 'body','avatar')