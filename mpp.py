import os
import shutil
from mutagen.mp3 import MP3
from pydub import AudioSegment



## con esto basta ´para conocer la duracion del archivo mp3
#audio= MP3('archivo.mp3')
#duracion=(audio.info.length)

#esta es la carpeta donde estaran las llamadas de las ventas
#gsm='gsm'
carpetaventa='venta'
carpetanoventa='no_venta'
carpeta_destino = 'CARGUE DE LLAMADAS'

#en esta linea de codigo obtenemos una lista con todos los archivos de la carpeta
archivos=os.listdir(carpetaventa)
archivos2=os.listdir(carpetanoventa)
#gsmaudio=os.listdir(gsm)



#vamos a iterar en la carpeta
for archivo in archivos:
    #esta linea de codigo aun no se si implementarla, solo va a evaluar si el archivo termina en.mp3, de no ser asi no se usara
    #if archivo.endswith('.mp3')
    ruta_archivo_antes=os.path.join(carpetaventa, archivo)
    audio=MP3(ruta_archivo_antes)
    nombre_archivo, extencion =os.path.splitext(os.path.basename(ruta_archivo_antes))
    #nombre_archivo es el nombre del archivo
    #extension es la extencion del archivo, en este caso es '.mp3'

    duracion=int(audio.info.length) #input en segudos
    duracion_min = duracion // 60 #retorna minuos
    duracion2_seg = (duracion % 60)#multiplicar por 60
    #duracion = MP3(ruta_archivo_antes).info
    #duracion2_seg = int(duracion.length)
    #duracion_min = duracion2_seg // 60
    #duracion2_seg %= 60
    duracion_seg=str(duracion2_seg).rjust(2,"0")

    #atributos
    listan=nombre_archivo.split("_")
    numero=listan[4]
    ora=listan[5]
    cel=listan[3]
    motor=listan[2]
    cedu=listan[6]
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
    duraciont=(f"{duracion_min}{duracion_seg}")
    #complemento
    complemento="VENTA_ONE-CONTACT-MEDELLIN_TMK_CONVERGENTE_TMK"
    #hora y fecha
    hora=ora[0:2]+"-"+ora[2:4]+"-"+ora[4:6]
    fecha = numero[6:8] + "-" + numero[4:6] + "-" + numero[0:4]
    #prueba

    nuevo_nombre=f"{fecha}_{hora}_{duraciont}_{cel}_{cedu}_{complemento}_{campaña}{extencion}.mp3"
    print(nuevo_nombre)
    ruta_archivo_despues=os.path.join(carpetanoventa, nuevo_nombre)
    
    os.rename(ruta_archivo_antes, ruta_archivo_despues)
    print(duracion)
    print("archivo editado exitosa mente")
    

    #print(f"{archivo}: {duracion_min} min {duracion_seg} seg")
    #nombrearchivo=f"VENTA_{nombre_archivo}_{duracion_min}min{duracion_seg}seg"


for archivo in archivos2:
    #esta linea de codigo aun no se si implementarla, solo va a evaluar si el archivo termina en.mp3, de no ser asi no se usara
    #if archivo.endswith('.mp3')
    ruta_archivo_antes=os.path.join(carpetanoventa, archivo)
    audio=MP3(ruta_archivo_antes)
    nombre_archivo, extencion =os.path.splitext(os.path.basename(ruta_archivo_antes))
    #nombre_archivo es el nombre del archivo
    #extension es la extencion del archivo, en este caso es '.mp3'

    duracion=int(audio.info.length)
    duracion_min = duracion // 60
    duracion2_seg = (duracion % 60)
    #duracion_min=str(duracion1_min).rjust(2,"0")
    # duracion = MP3(ruta_archivo_antes).info
    #duracion2_seg = int(duracion.length)
    #duracion_min = duracion2_seg // 60
    #duracion2_seg %= 60
    duracion_seg=str(duracion2_seg).rjust(2,"0")

    #atributos
    listan=nombre_archivo.split("_")
    numero=listan[4]
    ora=listan[5]
    cel=listan[3]
    motor=listan[2]
    cedu=listan[6]
    #DEFINIR CAMPAÑA
    if motor=="skcp1medMotor" or motor=="skcp2medMotor" or motor=="skcp3medMotor" or motor=="skcp4medMotor" or motor=="skcp5medMotor" or motor=="skcp6medMotor":
        campaña="PORTABILIDAD"
    elif motor=="skmigra2medMotor" or motor=="skmigra1medMotor":
        campaña="MIGRACION"
    elif motor=="skhogarnumedMotor" or motor=="skhogarmedMotor" or motor=="skhogdthmedMotor":
        campaña="HOGAR"
    elif motor=="skhogarnumedManual" or motor=="skhogarmedManual" or motor=="skhogdthmedManual":
        campaña="HOGAR"
    else:
        campaña="HOGAR"
    duraciont=(f"{duracion_min}{duracion_seg}")
    #complemento
    complemento="NO-VENTA_ONE-CONTACT-MEDELLIN_TMK_CONVERGENTE_TMK"
    
    #hora y fecha
    hora=ora[0:2]+"-"+ora[2:4]+"-"+ora[4:6]
    fecha = numero[6:8] + "-" + numero[4:6] + "-" + numero[0:4]
    #prueba

    nuevo_nombre=f"{fecha}_{hora}_{duraciont}_{cel}_{cedu}_{complemento}_{campaña}{extencion}.mp3"
    ruta_archivo_despues=os.path.join(carpetanoventa, nuevo_nombre)
    
    os.rename(ruta_archivo_antes, ruta_archivo_despues)
    print(f"La duracion es {duracion} segundos")
    print("archivo editado exitosa mente")



for mpp in os.listdir(carpetaventa):
    ruta_archivo_origen = os.path.join(carpetaventa, mpp)
    ruta_archivo_destino = os.path.join(carpeta_destino, mpp)
    shutil.move(ruta_archivo_origen, ruta_archivo_destino)
for mpp in os.listdir(carpetanoventa):
    ruta_archivo_origen = os.path.join(carpetanoventa, mpp)
    ruta_archivo_destino = os.path.join(carpeta_destino, mpp)
    shutil.move(ruta_archivo_origen, ruta_archivo_destino)


