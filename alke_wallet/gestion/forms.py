from django import forms
from .models import Cliente
from django.contrib.auth.forms import AuthenticationForm

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'}),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': '912345678',
                'maxlength': '9'
            }),
        }

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono:
            if not telefono.isdigit():
                raise forms.ValidationError("El teléfono solo debe contener números.")
            if len(telefono) > 9:
                raise forms.ValidationError("El teléfono no puede tener más de 9 dígitos.")
        return telefono

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control aw-input',
                'placeholder': 'Usuario',
                'autofocus': True,
            }
        )
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control aw-input',
                'placeholder': 'Contraseña',
            }
        )
    )