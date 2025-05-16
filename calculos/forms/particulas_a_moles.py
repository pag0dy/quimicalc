from django import forms

class ParticulasAMolesForm(forms.Form):
    particulas = forms.FloatField(
        label="Número de partículas",
        min_value=0,
        help_text="Ingresa el número total de átomos, moléculas o iones"
    )
    tipo = forms.ChoiceField(
        label="Tipo de partícula",
        choices=[("moléculas", "Moléculas"), ("átomos", "Átomos"), ("iones", "Iones")]
    )