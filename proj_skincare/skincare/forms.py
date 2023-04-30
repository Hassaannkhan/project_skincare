from django import forms

from .models import Skincaredata



class dataform(forms.ModelForm):

    class Meta:

        model = Skincaredata

        fields = '__all__'

    