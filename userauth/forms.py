from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserForm(UserCreationForm):
    #add new field to the forms
    avatar = forms.ImageField(required=False)
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name','last_name','email')


class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username','first_name', 'last_name','email','avatar']