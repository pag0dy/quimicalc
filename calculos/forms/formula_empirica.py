from django import forms

class FormulaEmpiricaForm(forms.Form):
    datos = forms.CharField(
        max_length=200,
        help_text="Usa el formato: C=40, H=6.71, O=53.29"
    )