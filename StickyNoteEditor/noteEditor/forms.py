from django import forms
from django.contrib.auth.models import User
from .models import StickyNote

class NoteForm(forms.ModelForm):

    class Meta:
        model = StickyNote
        fields = ['noteHead', 'noteBody']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']