# 🚗 Monitor de Tráfico y Movilidad Urbana en Lima

Este proyecto es un script de Python diseñado para monitorear en tiempo real las condiciones del tráfico en rutas clave de Lima, Perú, utilizando la API de Google Maps. El objetivo es capturar, procesar y almacenar datos de movilidad para su posterior análisis.

## ✨ Características Principales

* **Consulta en Tiempo Real:** Se conecta a la API de Google para obtener la duración y distancia de viaje actual, considerando las condiciones de tráfico.
* **Procesamiento de Datos:** Utiliza la librería **Pandas** para estructurar la información obtenida en un formato claro y tabular.
* **Almacenamiento Histórico:** Guarda los datos recopilados en archivos **CSV**, creando un registro diario que permite análisis a futuro.
* **Configuración Segura:** Las claves de API se manejan de forma segura en un archivo local (`config.py`) que es ignorado por Git a través del `.gitignore` para no exponer credenciales sensibles.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python
* **Librerías:** Pandas, googlemaps
* **API:** Google Maps Directions API
* **Control de Versiones:** Git y GitHub

## 🚀 Posibles Mejoras a Futuro

* **Automatización:** Configurar un flujo de trabajo con GitHub Actions para que el script se ejecute automáticamente a distintas horas del día.
* **Visualización:** Crear un dashboard interactivo en Looker Studio o Power BI conectado a los datos para visualizar las rutas y la variación del tráfico.
* **Análisis de Datos:** Utilizar los datos históricos para analizar patrones, como la diferencia de tráfico entre días de semana y fines de semana.