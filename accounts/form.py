from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.contrib.auth.hashers import check_password
from phone_field import PhoneField

from .models import MyUser, Send_email
from scraping import models

User=get_user_model()
class UserLoginForm(forms.Form):

    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'ismingizni kiriting'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'parolni kiriting'}))

    class Meta:
        model = MyUser
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
class register(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'ismingizni kiriting'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'familangizni kiriting'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'emailni kiriting'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'usernameni kiriting'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'parolni kiriting'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'parolni qaytadan kiriting'}))
    Rezume = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    class Meta:
        model=MyUser
        fields=('first_name','last_name','email','username','password1','password2','Rezume')
    def __init__(self,*args,**kwargs):
        super(register, self).__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class ContactForm(forms.Form):
    city = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    language = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}),label='Email')
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Username')
    class Meta:
        model=MyUser
        field=('city','language','send_email','username')

class UserUpdateForm(forms.Form):
    city = forms.ModelChoiceField(queryset=models.City.objects.all(), to_field_name='slug', required=True,
                                  widget=forms.Select(attrs={'class': 'form-select'}))
    language = forms.ModelChoiceField(queryset=models.Language.objects.all(), to_field_name='slug', required=True,
                                      widget=forms.Select(attrs={'class': 'form-select'}))
    send_email=forms.BooleanField(widget=forms.CheckboxInput,required=False)

    class Meta:
        model=Send_email
        field=('city','language','send_email','username')
class profile(UserChangeForm):
    username=forms.CharField(widget=forms.TextInput(),required=True)
    email=forms.CharField(widget=forms.EmailInput(attrs={'readonly':True}))
    file=forms.FileField(widget=forms.FileInput(),required=False)
    image=forms.ImageField(widget=forms.FileInput(),required=False)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'parolni kiriting'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'parolni qaytadan kiriting'}))
    class Meta:
        model=MyUser
        fields=('first_name','last_name', 'email','username','password1','password2','file')

    def __init__(self, *args, **kwargs):
        super(profile, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class']='custom-file-input'




