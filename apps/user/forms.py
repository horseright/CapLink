from django import forms

from .models import AMl


class IdentityCertificationForm(forms.ModelForm):
    class Meta:
        model = AMl
        exclude = ('user', )
