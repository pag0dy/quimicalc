from django.urls import path
from .views import (
    calcular_moles_view, 
    calcular_masa_molar_view, 
    home_view, 
    calcular_composicion_view, 
    calcular_formula_empirica_view,
    calcular_formula_molecular_view
)

urlpatterns = [
    path("", home_view, name="home"),
    path("moles/", calcular_moles_view, name="calculo_moles"),
    path("masa-molar/", calcular_masa_molar_view, name="calculo_masa_molar"),
    path("composicion/", calcular_composicion_view, name="calculo_composicion"),
    path("formula-empirica/", calcular_formula_empirica_view, name="calculo_formula_empirica"),
    path("formula-molecular/", calcular_formula_molecular_view, name="calculo_formula_molecular"),
]
