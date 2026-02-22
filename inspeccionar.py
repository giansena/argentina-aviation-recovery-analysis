import pandas as pd

df = pd.read_csv("vuelos_unificados_2019_2025.csv", nrows=5)

print("--- TUS COLUMNAS DISPONIBLES ---")
for col in df.columns:
    print(f"- {col}")

print("\n--- VISTA PREVIA ---")
print(df.head())