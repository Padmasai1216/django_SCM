from dataclasses import field
from logging import PlaceHolder
from django import forms
from django.contrib.auth.models import User
from django import forms

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label= ("Password"),
        widget=forms.PasswordInput())
    password2 = forms.CharField(label= ("Password confirmation"),
        widget=forms.PasswordInput(),
        help_text= ("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("username", "email",)
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user