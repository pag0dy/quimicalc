from django import forms

class ComposicionForm(forms.Form):
    formula = forms.CharField(label="Fórmula química", max_length=50)