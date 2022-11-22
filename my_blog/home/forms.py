from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label="username", 
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Nombre de usuario',
                'required':'True',
            }
        ),    
    )
    
    first_name = forms.CharField(
        label="Nombre", 
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Nombre',
                'required':'True',
            }
        ),
    )
    
    last_name = forms.CharField(
        label="Apellido", 
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Apellido',
                'required':'True',
            }
        ),
    )
    
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(
          attrs={
                'class':'form-control',
                'placeholder':'Correo',
                'required':'True',
            }  
        ),
    )
    
    password1 = forms.CharField(
        label="Password", 
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Password',
                'required':'True',
            } 
        ),
    )
    
    password2 = forms.CharField(
        label="Confirmar Password", 
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Confirmar Password',
                'required':'True',
            } 
        ),
    )
    
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
        
class UserUpdateForm(UserChangeForm):
    password = None
    
    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
        ]
        
        widgets = {
            "email": forms.TextInput(attrs={'class':'form-control', "required": "True"}),
            "first_name": forms.TextInput(attrs={'class':'form-control','required':'True',}),
            "last_name": forms.TextInput(attrs={'class':'form-control','required':'True',}),
        }