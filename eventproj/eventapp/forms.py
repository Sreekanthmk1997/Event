from .models import Service

from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'


class ServiceForm(forms.ModelForm):
    class Meta:
        model=Service
        fields='__all__'

        widgets={
            'booking_date':DateInput(),
        }


        labels={
            'cus_name':'Name:',
            'cus_ph':'Contact Number:',
            'cus_email': 'Email-ID:',
            'name':'Event Name:',
            'booking_date':'Booking Date:',
        }


class ReviewForm(forms.Form):
    cus_name = forms.CharField(
        label='Name', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Full name', 'id': 'form-firstname'}))
    cus_email = forms.EmailField(
        max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'E-mail', 'id': 'form-email'}))
    name = forms.CharField(
        label="Event Name", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))
    booking_date = forms.DateField(
        label="Event Name", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))




# class BookingForm(forms.Form):
#     user_email = forms.EmailField()
#     booking_details = forms.CharField(widget=forms.Textarea)