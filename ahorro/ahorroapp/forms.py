from django import forms
from ahorroapp.models import Detalle

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Detalle
        fields = '__all__'
