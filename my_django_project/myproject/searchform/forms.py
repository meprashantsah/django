from django import forms

class BookSearchForm(forms.Form):
    q = forms.CharField(label='search for books',max_length=100)
    