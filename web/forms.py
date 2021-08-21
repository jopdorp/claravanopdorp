from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    phone_number = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['placeholder'] = 'Your name'
        self.fields['email_address'].widget.attrs['placeholder'] = 'Your email'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Your phone number'
        self.fields['message'].widget.attrs['placeholder'] = 'Description of your project, questions?, looking for collaborations? '
        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['rows'] = 3


