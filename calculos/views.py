from django.shortcuts import render
from .forms.moles import MolesForm
from .forms.masa_molar import MasaMolarForm
from .services.moles import calcular_moles
from .services.masa_molar import calcular_masa_molar
from .forms.composicion import ComposicionForm
from .services.composicion import calcular_composicion_porcentual
from .forms.formula_empirica import FormulaEmpiricaForm
from .services.formulas import calcular_formula_empirica, parsear_composicion
from .forms.formula_molecular import FormulaMolecularForm
from .services.formulas import calcular_formula_molecular


def home_view(request):
    return render(request, "calculos/home.html")

def calcular_moles_view(request):
    resultado = None
    if request.method == "POST":
        form = MolesForm(request.POST)
        if form.is_valid():
            masa = form.cleaned_data["masa"]
            masa_molar = form.cleaned_data["masa_molar"]
            resultado = calcular_moles(masa, masa_molar)
    else:
        form = MolesForm()

    return render(request, "calculos/moles.html", {"form": form, "resultado": resultado})

def calcular_masa_molar_view(request):
    resultado = None
    error = None

    if request.method == "POST":
        form = MasaMolarForm(request.POST)
        if form.is_valid():
            formula = form.cleaned_data["formula"]
            try:
                resultado = calcular_masa_molar(formula)
            except Exception as e:
                error = f"Error al calcular la masa molar: {str(e)}"
    else:
        form = MasaMolarForm()

    return render(request, "calculos/masa_molar.html", {
        "form": form,
        "resultado": resultado,
        "error": error
    })

def calcular_composicion_view(request):
    resultado = None
    error = None

    if request.method == "POST":
        form = ComposicionForm(request.POST)
        if form.is_valid():
            formula = form.cleaned_data["formula"]
            try:
                resultado = calcular_composicion_porcentual(formula)
            except Exception as e:
                error = f"Error al calcular la composición: {str(e)}"
    else:
        form = ComposicionForm()

    return render(request, "calculos/composicion.html", {
        "form": form,
        "resultado": resultado,
        "error": error
    })

def calcular_formula_empirica_view(request):
    resultado = None
    error = None

    if request.method == "POST":
        form = FormulaEmpiricaForm(request.POST)
        if form.is_valid():
            try:
                datos = form.cleaned_data["datos"]
                masas = parsear_composicion(datos)
                resultado = calcular_formula_empirica(masas)
            except Exception as e:
                error = f"Error: {str(e)}"
    else:
        form = FormulaEmpiricaForm()

    return render(request, "calculos/formula_empirica.html", {
        "form": form,
        "resultado": resultado,
        "error": error
    })

def calcular_formula_molecular_view(request):
    formula_molecular_str = None
    error = None

    if request.method == "POST":
        form = FormulaMolecularForm(request.POST)
        if form.is_valid():
            try:
                formula = form.cleaned_data["formula_empirica"]
                masa_molar = form.cleaned_data["masa_molar_real"]
                resultado = calcular_formula_molecular(formula, masa_molar)

                if isinstance(resultado, dict):
                    formula_molecular_str = "".join(
                        f"{el}{cant if cant > 1 else ''}"
                        for el, cant in resultado.items()
                    )
                else:
                    error = "El cálculo no devolvió una estructura válida."

            except Exception as e:
                error = f"Error: {str(e)}"
    else:
        form = FormulaMolecularForm()

    return render(request, "calculos/formula_molecular.html", {
        "form": form,
        "formula_str": formula_molecular_str,
        "error": error
    })