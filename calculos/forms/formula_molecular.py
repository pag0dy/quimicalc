from django import forms

class FormulaMolecularForm(forms.Form):
    formula_empirica = forms.CharField(label="Fórmula empírica", max_length=50)
    masa_molar_real = forms.FloatField(label="Masa molar real (g/mol)", min_value=0)