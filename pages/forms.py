from django import forms

class ContactForm(forms.Form):
    your_name = forms.CharField(max_length=100, label='Your name')
    email = forms.EmailField(required=False,label='Your email')
    password = forms.CharField(min_length=6,widget=forms.PasswordInput)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
