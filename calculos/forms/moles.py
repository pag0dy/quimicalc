from django import forms

class MolesForm(forms.Form):
    masa = forms.FloatField(label="Masa (g)", min_value=0)
    masa_molar = forms.FloatField(label="Masa molar (g/mol)", min_value=0.0001)