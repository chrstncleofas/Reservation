from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
  class Meta:
    model = Reservation
    fields = [
      'userID',
      'fname',
      'lname',
      'email',
      'phone',
    ]

    labels = {
      'userID' : 'User ID',
      'fname': 'First Name',
      'lname': 'Last Name',
      'email': 'Email',
      'phone': 'Phone',
    }
    widgets = {
      'userID': forms.TextInput(attrs={'class': 'form-control'}),
      'fname': forms.TextInput(attrs={'class': 'form-control'}),
      'lname': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'phone': forms.TextInput(attrs={'class': 'form-control'}),
    }
