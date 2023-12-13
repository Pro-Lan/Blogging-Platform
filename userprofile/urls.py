from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
    # 用戶登入
    path('login/', views.user_login, name='login'),
    # 用戶退出
    path('logout/', views.user_logout, name='logout'),
    
    # 用戶註冊
    path('register/', views.user_register, name='register'),
    
    # 用戶刪除
    path('delete/<int:id>/', views.user_delete, name='delete'),
    
     # 用戶信息
    path('edit/<int:id>/', views.profile_edit, name='edit'),
]