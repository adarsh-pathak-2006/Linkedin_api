from django import forms

class registerform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
    rep_password=forms.CharField(widget=forms.PasswordInput())