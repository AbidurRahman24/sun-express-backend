from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
# class AuthorForm(forms.ModelForm):
#     class Meta: 
#         model = Author
#         fields = '__all__'
#         # fields = ['name', 'bio']
#         # exclude = ['bio']

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    staff = forms.BooleanField(required=False)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'staff']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False 
        if commit:
            user.save()
        return user


class ChangeUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']