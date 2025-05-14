from django import forms

class FormulaEmpiricaForm(forms.Form):
    carbono = forms.FloatField(label="C (%)", min_value=0, required=False)
    hidrogeno = forms.FloatField(label="H (%)", min_value=0, required=False)
    oxigeno = forms.FloatField(label="O (%)", min_value=0, required=False)
    nitrogeno = forms.FloatField(label="N (%)", min_value=0, required=False)
    azufre = forms.FloatField(label="S (%)", min_value=0, required=False)
    # puedes agregar más elementos si lo necesitas