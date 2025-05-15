from django import forms

class AvogadroForm(forms.Form):
    moles = forms.FloatField(label="Cantidad de moles", min_value=0)
