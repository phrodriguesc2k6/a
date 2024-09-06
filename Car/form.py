from django import forms
from .models import Car


class formulario(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
    
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20.000:
            self.add_error('value', 'Valor Mínimo do carro deve ser de 20.000')
        return value

