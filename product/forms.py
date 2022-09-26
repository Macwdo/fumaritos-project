from django import forms
from .models import Produto


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        exclude = ['vendidos']
        widgets = {
            'marca': forms.TextInput(attrs={'class':'form-control'}),
            'puffs': forms.TextInput(attrs={'class':'form-control'}),
            'sabor': forms.TextInput(attrs={'class':'form-control'}),
            'custo': forms.NumberInput(attrs={'class':'form-control'}),
            'preco': forms.NumberInput(attrs={'class':'form-control'}),
            'estoque': forms.NumberInput(attrs={'class':'form-control'})
        }