import pandas as pd

archivo = "jet-fuel-60.xls"

try:
    # Como el archivo es HTML al final
    tablas = pd.read_html(archivo)
    
    print(f"Se encontraron {len(tablas)} tablas dentro del archivo.")
    
    # Prueba con la primera tabla encontrada
    df_fuel = tablas[0]
    
    print("\n--- COLUMNAS DETECTADAS ---")
    print(df_fuel.columns.tolist())
    
    print("\n--- VISTA PREVIA (10 filas) ---")
    print(df_fuel.head(10))
    
    # CVS real así no me da más problemas
    df_fuel.to_csv("jet_fuel_limpio.csv", index=False)
    print("\n¡Éxito! Se ha creado 'jet_fuel_limpio.csv' para trabajar mejor.")

except Exception as e:
    print(f"Error al intentar leer como HTML: {e}")