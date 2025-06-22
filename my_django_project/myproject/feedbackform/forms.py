from django import forms
from .models import Feedback

class FeedbackForm(forms.Form):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
        