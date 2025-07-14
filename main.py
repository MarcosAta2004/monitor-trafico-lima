import googlemaps
import pandas as pd
from datetime import datetime
import os
from config import API_KEY # Importamos nuestra clave secreta

# --- ¡CONFIGURACIÓN INICIAL! ---
# Define aquí las rutas que quieres monitorear. Puedes añadir más.
RUTAS = [
    {
        "nombre": "Javier Prado (mañana)",
        "origen": "Ovalo Huarochiri, La Molina, Peru",
        "destino": "Plaza San Martin, Lima, Peru"
    },
    {
        "nombre": "Panamericana Sur",
        "origen": "Puente Atocongo, San Juan de Miraflores, Peru",
        "destino": "Puente Benavides, Santiago de Surco, Peru"
    }
]

# --- CÓDIGO DEL PROGRAMA ---

def obtener_datos_viaje(cliente_gmaps, origen, destino):
    """Obtiene el tiempo de viaje actual entre un origen y un destino."""
    try:
        ahora = datetime.now()
        resultado = cliente_gmaps.directions(origen,
                                           destino,
                                           mode="driving",
                                           departure_time=ahora)
        
        # Extraemos la duración en minutos del primer resultado de la ruta
        if resultado:
            pierna = resultado[0]['legs'][0]
            duracion_min = round(pierna['duration']['value'] / 60)
            distancia_km = round(pierna['distance']['value'] / 1000, 1)
            return duracion_min, distancia_km
        
    except Exception as e:
        print(f"Error al obtener la ruta entre {origen} y {destino}: {e}")
    
    return None, None

def main():
    """Función principal del script."""
    print("Iniciando monitor de tráfico...")
    cliente_gmaps = googlemaps.Client(key=API_KEY)
    
    datos_recopilados = []
    timestamp_actual = datetime.now()

    for ruta in RUTAS:
        nombre_ruta = ruta["nombre"]
        origen = ruta["origen"]
        destino = ruta["destino"]
        
        print(f"Consultando ruta: '{nombre_ruta}'...")
        duracion, distancia = obtener_datos_viaje(cliente_gmaps, origen, destino)
        
        if duracion is not None:
            datos_recopilados.append({
                "ruta_nombre": nombre_ruta,
                "origen": origen,
                "destino": destino,
                "timestamp": timestamp_actual.strftime("%Y-%m-%d %H:%M:%S"),
                "duracion_minutos": duracion,
                "distancia_km": distancia
            })

    if not datos_recopilados:
        print("No se pudo recopilar ningún dato. Terminando script.")
        return

    # Convertir los datos a un DataFrame de Pandas
    df = pd.DataFrame(datos_recopilados)

    # Guardar los datos en un archivo CSV
    nombre_archivo = f"trafico_{timestamp_actual.strftime('%Y%m%d')}.csv"
    ruta_archivo = os.path.join("data", nombre_archivo)
    
    # Si el archivo ya existe, añade los datos sin escribir el encabezado de nuevo
    if os.path.exists(ruta_archivo):
        df.to_csv(ruta_archivo, mode='a', header=False, index=False)
    else:
        df.to_csv(ruta_archivo, mode='w', header=True, index=False)

    print("-" * 30)
    print(f"¡Éxito! Datos guardados correctamente en: {ruta_archivo}")
    print("Resumen de datos:")
    print(df)


if __name__ == "__main__":
    main()