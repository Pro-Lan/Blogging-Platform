from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile

# 定義一個行內 admin
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'UserProfile'

# 將 Profile 關聯到 User 中
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# 重新注冊 User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)