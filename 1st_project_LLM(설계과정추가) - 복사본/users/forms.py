from django import forms
from users.models import Post, User
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "contents",
        ]
        widgets = {
            "contents": forms.Textarea(
                attrs={
                    "placeholder": "건의 사항....",
                }
            )
        }

class LoginForm(forms.Form):
    username = forms.CharField(
        min_length = 3,
        widget=forms.TextInput(
            attrs={"placeholder": "사용자명 (3자리 이상)"},
        ),
    )
    password = forms.CharField(
        min_length = 4,
        widget=forms.PasswordInput(
            attrs={"placeholder": "비밀번호 (4자리 이상)"}
        ),
    )

class SignupForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data["username"]

        if User.objects.filter(username=username).exists():
            raise ValidationError(f"입력한 사용자명({username})은 이미 사용 중 입니다")
        
        return username
    
    def clean(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            self.add_error("password2", "비밀번호와 비밀번호 확인란의 값이 다릅니다")

    def save(self):
        username = self.cleaned_data["username"]
        password1 = self.cleaned_data["password1"]


        user = User.objects.create_user(
            username = username,
            password = password1,
        )
        return user