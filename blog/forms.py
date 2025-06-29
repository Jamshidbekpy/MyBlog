from django.forms import ModelForm,Form, CharField, PasswordInput, TextInput, Textarea
from .models import Post, Comment, CustomUser
from django.contrib.auth.hashers import make_password

class UserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'image')
    def save(self, commit = True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
class LoginForm(Form):
    username = CharField(max_length=150)
    password = CharField(widget=PasswordInput)
      
    
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']  
        widgets = {
            'comment': Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
            })
        }
        
    def save(self, commit=True):
        instance = super().save(commit=False)  
        if commit:
            instance.save()
        return instance