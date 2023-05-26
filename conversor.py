import os
import sox

archivos = os.listdir("gsm")
carpeta_gsm = "gsm/"
carpeta_salida = "carpeta_cargue/"

for archivo in archivos:
    print(archivo)
    transformer = sox.Transformer()
    transformer.set_input_format(file_type='gsm')
    transformer.build(f"{carpeta_gsm}/{archivo}", f"{carpeta_salida}{archivo[:-4]}.mp3")
    os.remove(f"{carpeta_gsm}{archivo}")