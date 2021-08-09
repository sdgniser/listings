from django import forms

from .models import Listing

class SearchForm(forms.Form):
    query = forms.CharField(max_length = 200)
    sort_by = forms.CharField(max_length = 100)

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'category', 'price', 'location', 'condition',
                  'description', 'photo', 'op', 'email', 'phone']
