import pandas as pd

# 1- Carga
df_vuelos = pd.read_csv("resumen_vuelos_mensual.csv")
df_fuel = pd.read_csv("jet_fuel_limpio.csv")

# 2- datos en fecha real
df_fuel['fecha_dt'] = pd.to_datetime(df_fuel['Month'], format='%b %Y')
df_fuel['año'] = df_fuel['fecha_dt'].dt.year
df_fuel['mes'] = df_fuel['fecha_dt'].dt.month

# 3-
df_final = pd.merge(df_vuelos, df_fuel[['año', 'mes', 'Price']], on=['año', 'mes'], how='left')

# 4- métricas clave
df_final['vuelos_totales'] = df_final['cabotaje'] + df_final['internacional']

# 5- guardado de archivo maestro
df_final.to_csv("dataset_final_investigacion.csv", index=False)

print("--- VISTA PREVIA DEL DATASET FINAL ---")
print(df_final.sort_values(['año', 'mes']).head(15))

print("\n" + "="*40)
print("¡FASE  FINALIZADA!")
print("Archivo generado: dataset_final_investigacion.csv")
print("="*40)