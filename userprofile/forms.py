from django import forms
from django.contrib.auth.models import User
from .models import Profile

# 登錄表單，繼承了 forms.Form 類
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


# 註冊用戶表單
class UserRegisterForm(forms.ModelForm):
    # 覆寫 User 的密碼
    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email')

    # 對兩次輸入的密碼是否一致進行檢查
    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            raise forms.ValidationError("密碼輸入不一致,請重試。")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'bio')