import pandas as pd

print("Cargando el dataset gigante... por favor espera.")
# archivo unificado
df = pd.read_csv("vuelos_unificados_2019_2025.csv", low_memory=False)

# 1- Unificación de columnas
df['fecha_limpia'] = df['ï»¿fecha'].fillna(df['ï»¿fecha utc'])

df['clase_vuelo'] = df['clase de vuelos (todos los vuelos)'].fillna(df['clase de vuelo (todos los vuelos)'])

df['clasificacion_vuelo_limpia'] = df['clasificacion vuelo'].fillna(df['clasificaciã³n vuelo'])

df['tipo_movimiento_limpio'] = df['tipo movimiento'].fillna(df['tipo de movimiento'])

# 2- Selección de lo que me sirve jaja
columnas_finales = [
    'fecha_limpia', 
    'clase_vuelo', 
    'clasificacion_vuelo_limpia', 
    'tipo_movimiento_limpio', 
    'pasajeros',
    'pax'
]
df_reducido = df[columnas_finales].copy()

# 3- limpieza del formato de fecha
print("Formateando fechas...")
df_reducido['fecha_dt'] = pd.to_datetime(df_reducido['fecha_limpia'], dayfirst=True, errors='coerce')

# Borrado filas que no tengan fecha válida
df_reducido = df_reducido.dropna(subset=['fecha_dt'])

# 4- agregar columnas de tiempo
df_reducido['año'] = df_reducido['fecha_dt'].dt.year
df_reducido['mes'] = df_reducido['fecha_dt'].dt.month

# 5- Dataset guardado para analizar
nombre_salida = "vuelos_listos_para_analisis.csv"
df_reducido.to_csv(nombre_salida, index=False)

print("\n" + "="*40)
print(f"¡LIMPIEZA COMPLETADA!")
print(f"Nuevo archivo: {nombre_salida}")
print(f"Columnas resultantes: {list(df_reducido.columns)}")
print("="*40)