from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# 用戶擴展信息
class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # 頭像
    avatar = models.ImageField(upload_to='avatar/%Y%m%d/', blank=True)
    # 簡介
    bio = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)
    

