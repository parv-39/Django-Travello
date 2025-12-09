from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'adults', 'children', 'start_date', 'end_date', 'contact_number']
        widgets = {
            'start_date' : forms.DateInput(attrs={'type': 'date'}),
            'end_date' : forms.DateInput(attrs={'type': 'date'}),
        }