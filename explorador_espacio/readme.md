# Scripts para Automatización de Simulaciones en gem5

Este conjunto de scripts permite automatizar el uso del simulador gem5 modificando los parámetros de un procesador base para realizar simulaciones y extraer información específica. 

## Descripción

Estos scripts están diseñados para generar combinaciones de configuraciones de parámetros para el simulador gem5, ejecutar simulaciones para cada combinación, y extraer datos relevantes de los resultados. Los parámetros a modificar se especifican en un diccionario y el programa genera automáticamente la combinatoria de todos ellos. Luego, ejecuta seis tareas de prueba para cada combinación y recopila los resultados en un archivo CSV llamado `utiles.csv`.

> **Nota:** los scripts deben colocarse en la carpeta `workloads` para funcionar correctamente.

## Estructura de Funcionamiento

1. **Definición de Parámetros**: Se definen los parámetros a cambiar dentro de un diccionario en el script. Cada clave representa un parámetro específico del procesador y su valor una lista de opciones posibles.

2. **Generación de Combinaciones**: El programa crea todas las combinaciones posibles de los valores proporcionados en el diccionario.

3. **Ejecución de Simulaciones**: Para cada combinación generada, se ejecutan seis tareas de prueba en gem5.

4. **Extracción de Resultados**: Al finalizar cada simulación, el programa busca los archivos resultantes, extrae la información relevante y la almacena en `utiles.csv`.

## Configuración

- **Carpeta**: Asegúrate de colocar estos scripts en la carpeta `workloads`.
- **Archivos Resultantes**: Los archivos resultantes deben tener el formato y la estructura necesarios para permitir una extracción de datos automatizada.
- **Diccionario de Parámetros**: Modifica el diccionario de parámetros en el script según los valores y parámetros de gem5 que deseas explorar.

## Resultados

Todos los resultados se almacenarán en un archivo `utiles.csv` dentro de la carpeta raíz del proyecto. Este archivo incluye los datos extraídos de cada combinación de parámetros probada, lo que permite un análisis posterior de rendimiento y características de las configuraciones simuladas.

## Requerimientos

- **gem5**: Este simulador debe estar correctamente instalado y accesible desde el entorno donde se ejecutan los scripts.
- **Python 3.x**: Los scripts están escritos en Python, por lo que es necesario un entorno de ejecución compatible.

## Ejecución

1. Coloca los scripts en la carpeta `workloads`.
2. Modifica el diccionario de parámetros en el script para definir las configuraciones a probar.
3. Ejecuta el script principal para iniciar las simulaciones en gem5.
4. Revisa el archivo `utiles.csv` para ver los resultados generados.

---

Este README organiza la información y brinda detalles adicionales que deberían ayudar a los usuarios a entender mejor cómo usar los scripts y qué esperar de los resultados.
