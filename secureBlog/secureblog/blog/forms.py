from .models import Comment, Post
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms
from captcha.fields import CaptchaField


class CommentForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Comment
        fields = ('comment',)
        prepopulated_fields = {'visible': (False,)}

    def save_model(self, request, obj, form, change):
        obj.user = request.user.username
        super().save_model(request, obj, form, change)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'abstract', 'content', 'status')
#        widgets = {
#            'content': SummernoteInplaceWidget(),
#        }

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        permissions = ('read_articles')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.username = self.cleaned_data["username"]
        if commit:
            user.save()
        return user