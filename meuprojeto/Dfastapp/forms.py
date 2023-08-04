from django import forms

class login_form (forms.Form):
    usuario = forms.CharField(max_length=50) 
    senha = forms.CharField(widget=forms.PasswordInput)   


