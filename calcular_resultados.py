import pandas as pd

print("Analizando datos... unificando nombres de columnas.")
df = pd.read_csv("vuelos_listos_para_analisis.csv", low_memory=False)

# 1- Agrupación por Año, Mes y Clasificación
resumen_mensual = df.groupby(['año', 'mes', 'clasificacion_vuelo_limpia']).size().reset_index(name='total_vuelos')

# 2- Pivotear
df_final = resumen_mensual.pivot_table(
    index=['año', 'mes'], 
    columns='clasificacion_vuelo_limpia', 
    values='total_vuelos', 
    aggfunc='sum'
).reset_index()

# 3- NORMALIZACIÓN AGRESIVA (Traducción de términos ANAC)
df_final.columns = [str(col).lower().strip() for col in df_final.columns]

# Unificación de todo lo que sea Doméstico/Cabotaje
cols_cabotaje = ['doméstico', 'domã©stico', 'dom', 'cabotaje']
df_final['cabotaje_final'] = df_final[[c for c in cols_cabotaje if c in df_final.columns]].sum(axis=1)

# Unificación de todo lo que sea Internacional
cols_inter = ['internacional', 'inter']
df_final['internacional_final'] = df_final[[c for c in cols_inter if c in df_final.columns]].sum(axis=1)

# Solo las columnas limpias
df_resumen = df_final[['año', 'mes', 'cabotaje_final', 'internacional_final']].copy()
df_resumen = df_resumen.rename(columns={'cabotaje_final': 'cabotaje', 'internacional_final': 'internacional'})

# 4- Guardar
df_resumen.to_csv("resumen_vuelos_mensual.csv", index=False)

# 5- Cálculo de resultados
print("\n--- RESULTADOS PRELIMINARES ---")
v_2019 = df_resumen[df_resumen['año'] == 2019]['cabotaje'].sum()
v_2020 = df_resumen[df_resumen['año'] == 2020]['cabotaje'].sum()

if v_2019 > 0:
    caida = ((v_2020 - v_2019) / v_2019) * 100
    print(f"Total vuelos Cabotaje 2019: {v_2019:,.0f}")
    print(f"Total vuelos Cabotaje 2020: {v_2020:,.0f}")
    print(f"Magnitud de la caída (Impacto Pandemia): {caida:.2f}%")
else:
    print("No se encontraron datos de 2019 para comparar.")

print("\n¡Listo! Archivo 'resumen_vuelos_mensual.csv' unificado.")