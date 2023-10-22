from django import forms
from website.models import Contact


# Creating a simple form for capturing the name, email, subject, and message
class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    Subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)


# Creating a form based on the Contact model
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
