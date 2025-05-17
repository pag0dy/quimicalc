from django import forms

class MolesForm(forms.Form):
    masa = forms.FloatField(label="Masa", min_value=0)
    unidad = forms.ChoiceField(
        label="Unidad de masa",
        choices=[
            ("ug", "µg"),
            ("mg", "mg"),
            ("g", "g"),
            ("kg", "kg"),
            ("ton", "tonelada")
        ]
    )
    masa_molar = forms.FloatField(label="Masa molar (g/mol)", min_value=0.0001)