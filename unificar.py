import pandas as pd
import os

# busqueda de archivos scv sin importar las mayusculas o minusculas
archivos = [f for f in os.listdir('.') if f.lower().endswith('.csv') and "unificados" not in f.lower()]

lista_vuelos = []

print(f"Directorio actual: {os.getcwd()}")
print(f"Archivos detectados: {archivos}\n")

if not archivos:
    print("No se encontraron archivos CSV.")
else:
    for f in archivos:
        try:
            # Quitamos 'low_memory' para que no de error con el motor de python
            # 'sep=None' detectará si es coma o punto y coma automáticamente
            df = pd.read_csv(f, sep=None, engine='python', encoding='latin1')
            
            # Limpiamos nombres de columnas
            df.columns = df.columns.str.strip().str.lower()
            
            # Guardamos el origen
            df['fuente_archivo'] = f
            
            lista_vuelos.append(df)
            print(f" OK: {f} cargado con {len(df)} filas.")
            
        except Exception as e:
            print(f" ERROR al leer {f}: {e}")

    if lista_vuelos:
        print("\nConcatenando archivos... esto puede tardar unos segundos.")
        df_final = pd.concat(lista_vuelos, ignore_index=True)
        
        nombre_salida = "vuelos_unificados_2019_2025.csv"
        df_final.to_csv(nombre_salida, index=False, encoding='utf-8')
        
        print("\n" + "="*40)
        print(f"¡PROCESO EXITOSO!")
        print(f"Archivo generado: {nombre_salida}")
        print(f"Total de registros combinados: {len(df_final)}")
        print("="*40)
    else:
        print("\nNo se pudo unificar nada.")