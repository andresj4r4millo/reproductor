import os
import sox

carpeta_gsm = "gsm"
carpeta_salida = "carpeta_cargue"

archivos = os.listdir(carpeta_gsm)

import sox

def gsm_a_mp3(archivo_entrada, archivo_salida):
    transformer = sox.Transformer()

    transformer.set_input_format(file_type='gsm')

    transformer.build(archivo_entrada, archivo_salida)

archivo_entrada_path = 'gsm/gsm.gsm'
archivo_salida_path = 'f{carpeta_salida}/file.mp3'

gsm_a_mp3(archivo_entrada_path, archivo_salida_path)
