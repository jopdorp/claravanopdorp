from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    phone_number = forms.NumberInput()
    message = forms.CharField(widget=forms.Textarea, max_length=2000)

