from django import forms
from django.core import validators
from formsApp.models import Project


class ContactForm(forms.Form):
    """ContactForm definition."""
    fullname = forms.CharField(widget=forms.TextInput(attrs={'id': 'fname', 'placeholder': 'Enter your full name', 'class': 'form-control'}),
                               validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(20)])
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'enter your email address', 'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'enter your content here', 'class': 'form-conrol'}))


class ProjectForm(forms.ModelForm):
    """Form definition for MODELNAME."""
    class Meta:
        """Meta definition for MODELNAMEform."""
        model = Project
        fields = "__all__"
