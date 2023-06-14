import os
import sox

def convertir_llamadas():
    # Listar los archivos en el directorio "carpeta_cargue"
    archivos = os.listdir("carpeta_cargue")

    # Define la ruta de la carpeta
    carpeta_cargue = "carpeta_cargue/"

    # Iterar sobre cada archivo en la lista de archivos
    for archivo in archivos:
        if archivo.endswith(".gsm"):
    
            # Crear una instancia del objeto Transformer de sox
            transformer = sox.Transformer()

            # Establecer el formato de entrada como 'gsm'
            transformer.set_input_format(file_type='gsm')

            # Construir la transformación: convertir el archivo de entrada a MP3 en la carpeta de salida
            transformer.build(f"{carpeta_cargue}/{archivo}", f"{carpeta_cargue}{archivo[:-4]}.mp3")

            # Eliminar el archivo original de la carpeta de entrada
            os.remove(f"{carpeta_cargue}{archivo}")