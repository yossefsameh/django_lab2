from django import forms
from amazon.models import Cars

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'