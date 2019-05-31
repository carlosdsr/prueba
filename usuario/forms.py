from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','cedula','email','cargo','password','codigoEmpleado',)



