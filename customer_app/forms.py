from django import forms

from .models import HelpRequest


class HelpRequestForm(forms.ModelForm):
    class Meta:
        model = HelpRequest
        fields = ["full_name", "email", "issue_category", "description"]
