from django import forms
from advert.models import Advert

class AdvertForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = ('title', 'text', 'picture', 'category', 'price')