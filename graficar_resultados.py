import pandas as pd
import matplotlib.pyplot as plt

# 1- Cargar del dataset maestro
df = pd.read_csv("dataset_final_investigacion.csv")

# Para que el precio se lea estrictamente como número
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# 2- Fecha real para que el gráfico sea continuo
df['fecha'] = pd.to_datetime(df['año'].astype(str) + '-' + df['mes'].astype(str) + '-01')
df = df.sort_values('fecha')

# 3- Configurar el gráfico
fig, ax1 = plt.subplots(figsize=(14, 7))

# Eje izquierdo: Volumen de Vuelos (Azul)
ax1.set_xlabel('Año / Mes')
ax1.set_ylabel('Cantidad de Vuelos Totales', color='navy', fontsize=12, fontweight='bold')
ax1.plot(df['fecha'], df['vuelos_totales'], color='blue', label='Vuelos', linewidth=3)
ax1.fill_between(df['fecha'], df['vuelos_totales'], color='blue', alpha=0.1)
ax1.tick_params(axis='y', labelcolor='navy')
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.set_ylim(bottom=0) # Obligamos a los vuelos a empezar visualmente en 0

# Eeje derecho: Precio Jet Fuel (Rojo)
ax2 = ax1.twinx()
ax2.set_ylabel('Precio Jet Fuel (USD / Gallón)', color='red', fontsize=12, fontweight='bold')

# Filtrar para graficar solamete los meses que tienen precio de combustible
df_fuel = df.dropna(subset=['Price'])
ax2.plot(df_fuel['fecha'], df_fuel['Price'], color='red', linestyle='--', label='Precio Fuel', linewidth=2.5)
ax2.tick_params(axis='y', labelcolor='red')

# Forzar que el eje de precios arranque en 0
# y le darle un 10% de margen arriba para que respire
ax2.set_ylim(bottom=0, top=df_fuel['Price'].max() * 1.1)

# 4- Título y detalles
plt.title('Estudio de Vuelos en Pandemia: Impacto, Inflexión y Combustible', fontsize=16, pad=15)
fig.tight_layout()

# 5- Guardar el resultado
plt.savefig('analisis_final_vuelos_corregido.png')
print("\n" + "="*40)
print("¡GRÁFICO CORREGIDO EXITOSAMENTE!")
print("Revisá 'analisis_final_vuelos_corregido.png'.")
print("="*40)

plt.show()