from django.urls import path
from . import views
# 正在部署的應用的名稱
app_name = 'article'

urlpatterns = [
    #文章列表
    path('article-list/', views.article_list, name='article_list'),
    # 文章詳情
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    # 寫文章
    path('article-create/', views.article_create, name='article_create'),

    # 安全刪除文章
    path(
        'article-safe-delete/<int:id>/',
        views.article_safe_delete,
        name='article_safe_delete'
    ),
    
    # 更新文章
    path('article-update/<int:id>/', views.article_update, name='article_update'),
]