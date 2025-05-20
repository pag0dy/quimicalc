# 🧪 QuimiCalc

**QuimiCalc** es una aplicación web desarrollada en Python con Django para apoyar el aprendizaje de química general y aplicada. Permite resolver cálculos fundamentales relacionados con masa, moles, partículas, fórmulas químicas y más.

---

## 🚀 Funcionalidades

La app permite realizar los siguientes cálculos químicos:

| Cálculo                        | Descripción breve |
|-------------------------------|--------------------|
| **Moles (masa)**              | Calcula moles a partir de masa y masa molar |
| **Moles (partículas)**        | Convierte número de partículas en moles |
| **Partículas (moles)**        | Usa el número de Avogadro para calcular partículas |
| **Masa molar**                | Determina la masa molar a partir de una fórmula |
| **Masa atómica**              | Muestra la masa atómica promedio de un elemento |
| **Composición porcentual**    | Calcula el % de cada elemento en un compuesto |
| **Fórmula empírica**          | A partir de la composición, deduce la fórmula más simple |
| **Fórmula molecular**         | Calcula la fórmula molecular a partir de la empírica y la masa molar |

---

## 🖥️ Tecnologías utilizadas

- **Python** 3.11
- **Django** 4.x
- **HTML + CSS** (con MathJax para fórmulas)
- **periodictable** – para obtener datos atómicos reales
- **pyvalem** – para interpretar fórmulas químicas

---

## 🧮 Ejemplos de uso

- **¿Cuántos moles hay en 36 g de H₂O?**  
  Resultado: 2.00 mol

- **¿Cuál es la masa molar de Ca₃(PO₄)₂?**  
  Resultado: 310.18 g/mol

- **¿Cuántas moléculas hay en 0.25 mol de H₂O?**  
  Resultado: 1.51 × 10²³ moléculas

---

## 📦 Instalación local

```bash
git clone https://github.com/tuusuario/quimicalc.git
cd quimicalc
pip install -r requirements.txt
python manage.py runserver
```
---

## 🌐 Acceso en línea

https://quimicalc.onrender.com

---

	•	Proyecto realizado para: Química Aplicada a la Ingeniería
	•	Año: 2025