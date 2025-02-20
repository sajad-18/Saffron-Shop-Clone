from django import forms


class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Inter your username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Inter your email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Inter your password'}))


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Inter your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Inter your password'}))