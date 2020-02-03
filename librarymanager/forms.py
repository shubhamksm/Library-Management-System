from django import forms

class SearchForm(forms.Form):
  search_field = forms.CharField(label='Enter Book id', max_length=15)
