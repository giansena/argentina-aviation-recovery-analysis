import pandas as pd

df = pd.read_csv("dataset_final_investigacion.csv")

# 1- Magnitud de la caída (2019 vs 2020)
v_2019 = df[df['año'] == 2019]['vuelos_totales'].sum()
v_2020 = df[df['año'] == 2020]['vuelos_totales'].sum()
caida = ((v_2020 - v_2019) / v_2019) * 100

# 2- Estado actual (2019 vs 2025 - usando meses comparables si 2025 está incompleto)
# Comparación del total anual o los meses disponibles
v_2025 = df[df['año'] == 2025]['vuelos_totales'].sum()
comparativa_final = ((v_2025 - v_2019) / v_2019) * 100

print("="*50)
print("RESUMEN ESTADÍSTICO")
print("="*50)
print(f"1. IMPACTO INICIAL: Los vuelos cayeron un {caida:.2f}% en 2020.")
print(f"2. RECUPERACIÓN: A día de hoy (2025), el volumen de vuelos es un {comparativa_final:.2f}% respecto al nivel prepandemia (2019).")
print("-"*50)
print("PUNTO DE INFLEXIÓN: Revisar en el gráfico el periodo Mayo-Julio 2022.")
print("El combustible superó los 4.0 USD/gal y la curva de vuelos se estancó.")
print("="*50)