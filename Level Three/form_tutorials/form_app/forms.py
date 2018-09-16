from django import forms
from django.core import validators

class proto_Form(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Please enter your email again:')
    text = forms.CharField(widget = forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        
        if vmail != email:
            raise forms.ValidationError("It don't match ya fool!")
    

