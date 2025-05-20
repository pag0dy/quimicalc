from django import forms

class FormulaEmpiricaForm(forms.Form):
    datos = forms.CharField(
        max_length=200,
    )