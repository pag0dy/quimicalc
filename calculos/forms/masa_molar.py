from django import forms

class MasaMolarForm(forms.Form):
    formula = forms.CharField(label="Fórmula química", max_length=50)
    