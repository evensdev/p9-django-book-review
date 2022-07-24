# J'importe le module de formulaire
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


# SE CONNECTER
class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Entrez votre username"}), label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Entrez votre mot de passe"}), label='Mot de passe')


# CRÉER UN COMPTE

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=63, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Ajoutez un username"}), label='Nom d’utilisateur')

    email = forms.CharField(max_length=63, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Email"}), label='Email')

    password1 = forms.CharField(max_length=63, widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Ajoutez votre mot de passe"}), label='Mot de passe')

    password2 = forms.CharField(max_length=63, widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Répetez votre mot de passe"}), label='Confirmation du Mot de Passe')

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email')