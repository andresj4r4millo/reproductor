import os
import shutil
from mutagen.mp3 import MP3

#Esta función se ejecuta cuando se presiona el botón que clasifica una llamada como VENTA dentro de la interfaz del reproductor
def venta(archivos, carpeta_cargue):
    global nuevo_nombre
    archivo=archivos[0]

    ruta_archivo_antes=os.path.join(carpeta_cargue, archivo)
    audio=MP3(ruta_archivo_antes)
    duracion=int(audio.info.length) #duracion en segudos
    duracion_min = duracion // 60 #retorna minuos como entero
    duracion2_seg = (duracion % 60)
    duracion_seg=str(duracion2_seg).rjust(2,"0")
    duraciont=(f"{duracion_min}{duracion_seg}") #

    nombre_audio , extencion =os.path.splitext(os.path.basename(ruta_archivo_antes))

    listan=nombre_audio.split("_")
           
    numero=listan[3]
    ora=listan[4]
    cel=listan[2]
    motor=listan[1]
    cedu=listan[5]
        
    #DEFINIR CAMPAÑA
    if motor=="skcp1medMotor" or motor=="skcp2medMotor" or motor=="skcp3medMotor" or motor=="skcp4medMotor" or motor=="skcp5medMotor" or motor=="skcp6medMotor":
        campaña="PORTABILIDAD"
    elif motor=="skmigra1medMotor" or motor=="skmigra2medMotor":
        campaña="MIGRACION"
    elif motor=="skhogarnumedMotor" or motor=="skhogarmedMotor" or motor=="skhogdthmedMotor":
        campaña="HOGAR"
    elif motor=="skhogarnumedManual" or motor=="skhogarmedManual" or motor=="skhogdthmedManual":
        campaña="HOGAR"
    else:
        campaña="HOGAR"
    campañat=str(campaña)
    #duraciont=(f"{duracion_min}{duracion_seg}")

    #complemento
    complemento=str("VENTA_ONE-CONTACT-MEDELLIN_TMK_CONVERGENTE_TMK")
    #hora y fecha
    hora=ora[0:2]+"-"+ora[2:4]+"-"+ora[4:6]
    fecha = numero[6:8] + "-" + numero[4:6] + "-" + numero[0:4]
    nuevo_nombre=f"{fecha}_{hora}_{duraciont}_{cel}_{cedu}_{complemento}_{campañat}{extencion}"
    ruta_archivo_despues=os.path.join(carpeta_cargue, nuevo_nombre)
    #renombrar
    #here
    os.rename(ruta_archivo_antes ,ruta_archivo_despues)
    # enviar a carpeta exporte

#Esta función se ejecuta cuando se presiona el botón que clasifica una llamada como NO VENTA dentro de la interfaz del reproductor
def no_venta( archivos, carpeta_cargue):
    global nuevo_nombre
    archivo=archivos[0]
    
    ruta_archivo_antes=os.path.join(carpeta_cargue, archivo)
    audio=MP3(ruta_archivo_antes)
    duracion=int(audio.info.length) #input en segudos
    duracion_min = duracion // 60 #retorna minuos
    duracion2_seg = (duracion % 60)#multiplicar por 60
    
    duracion_seg=str(duracion2_seg).rjust(2,"0")
    duraciont=(f"{duracion_min}{duracion_seg}")
    nombre_audio , extencion =os.path.splitext(os.path.basename(ruta_archivo_antes))

    listan=nombre_audio.split("_")
           
    numero=listan[3]
    ora=listan[4]
    cel=listan[2]
    motor=listan[1]
    cedu=listan[5]
        
    #DEFINIR CAMPAÑA
    if motor=="skcp1medMotor" or motor=="skcp2medMotor" or motor=="skcp3medMotor" or motor=="skcp4medMotor" or motor=="skcp5medMotor" or motor=="skcp6medMotor":
        campaña="PORTABILIDAD"
    elif motor=="skmigra1medMotor" or motor=="skmigra2medMotor":
        campaña="MIGRACION"
    elif motor=="skhogarnumedMotor" or motor=="skhogarmedMotor" or motor=="skhogdthmedMotor":
        campaña="HOGAR"
    elif motor=="skhogarnumedManual" or motor=="skhogarmedManual" or motor=="skhogdthmedManual":
        campaña="HOGAR"
    else:
        campaña="HOGAR"
    campañat=str(campaña)
    #duraciont=(f"{duracion_min}{duracion_seg}")
    #complemento
    complemento=str("NO_VENTA_ONE-CONTACT-MEDELLIN_TMK_CONVERGENTE_TMK")
    #hora y fecha
    hora=ora[0:2]+"-"+ora[2:4]+"-"+ora[4:6]
    fecha = numero[6:8] + "-" + numero[4:6] + "-" + numero[0:4]
    nuevo_nombre=f"{fecha}_{hora}_{duraciont}_{cel}_{cedu}_{complemento}_{campañat}{extencion}"
    ruta_archivo_despues=os.path.join('carpeta_cargue', nuevo_nombre)
    #renombrar
    os.rename(ruta_archivo_antes,ruta_archivo_despues)
    # enviar a carpeta exporte

#Esta función se encarga de mover las llamadas de la carpeta de cargue a la carpeta de destino
def mover(llamadas, carpeta_destino='carpeta_destino'):
    llamada=llamadas[0]
    ruta_archivo_antes=os.path.join('carpeta_cargue', llamada)
    ruta_archivo_destino = os.path.join(carpeta_destino, llamada)
    shutil.move(ruta_archivo_antes, ruta_archivo_destino)