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
from .forms.avogadro import AvogadroForm
from .services.avogadro import calcular_particulas, calcular_moles_desde_particulas
from .forms.particulas_a_moles import ParticulasAMolesForm
from .services.utils import formatear_exponente, convertir_a_gramos


def home_view(request):
    return render(request, "calculos/home.html")

def calcular_moles_view(request):
    resultado_masa = None
    resultado_particulas = None
    tipo_particula = None
    error_particulas = None

    form_masa = MolesForm()
    form_particulas = ParticulasAMolesForm()

    if request.method == "POST":
        if request.POST.get("calculo") == "masa":
            form_masa = MolesForm(request.POST)
            if form_masa.is_valid():
                masa = form_masa.cleaned_data["masa"]
                unidad = form_masa.cleaned_data["unidad"]
                masa_molar = form_masa.cleaned_data["masa_molar"]
                masa_g = convertir_a_gramos(masa, unidad)
                resultado_masa = calcular_moles(masa_g, masa_molar)

        elif request.POST.get("calculo") == "particulas":
            form_particulas = ParticulasAMolesForm(request.POST)
            if form_particulas.is_valid():
                try:
                    particulas = form_particulas.cleaned_data["particulas"]
                    tipo_particula = form_particulas.cleaned_data["tipo"]
                    resultado_particulas = round(calcular_moles_desde_particulas(particulas), 2)
                except Exception as e:
                    error_particulas = f"Error: {str(e)}"

    return render(request, "calculos/moles.html", {
        "form_masa": form_masa,
        "form_particulas": form_particulas,
        "resultado_masa": resultado_masa,
        "resultado_particulas": resultado_particulas,
        "tipo_particula": tipo_particula,
        "error_particulas": error_particulas,
    })

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

def calcular_avogadro_view(request):
    resultado_html = None
    error = None

    if request.method == "POST":
        form = AvogadroForm(request.POST)
        if form.is_valid():
            try:
                moles = form.cleaned_data["moles"]
                resultado = calcular_particulas(moles)
                resultado_html = formatear_exponente(resultado)
            except Exception as e:
                error = f"Error: {str(e)}"
    else:
        form = AvogadroForm()

    return render(request, "calculos/avogadro.html", {
        "form": form,
        "resultado": resultado_html,
        "error": error
    })
