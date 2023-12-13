from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from article.views import article_list

urlpatterns = [
    path('admin/', admin.site.urls),
   
    #主頁
    path('', article_list, name='home'),
    
    path('article/', include('article.urls', namespace='article')),
    
    # 用戶管理
    path('userprofile/', include('userprofile.urls', namespace='userprofile')),
    
    # 評論
    path('comment/', include('comment.urls', namespace='comment')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
