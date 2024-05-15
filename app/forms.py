# app/forms.py

from django import forms
from .models import User, Reservation

class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['train', 'class_type', 'journey_date', 'from_place', 'to_place']

class CancellationForm(forms.Form):
    pnr_number = forms.CharField(max_length=20)
