from cafe.models import Comment
from django import forms

class CommentForm(forms.ModelForm): 
    class Meta: 
        model = Comment
        fields = [ 
            "menu_id",
            "content",
        ]
        widgets = {
            "content" : forms.Textarea(
                attrs={
                    "placeholder" : "댓글 달기..."
                }
            )
        }