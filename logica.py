import os
import shutil

carpeta_cargue='carpeta_cargue'
carpeta_destino='carpeta_destino'

def venta(archivo, duracion):
    nombre_llamada =archivo.split("/")
    nombre_llamada = nombre_llamada[-1]

    ruta_archivo_antes=os.path.join(carpeta_cargue, archivo)

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
    #duraciont=(f"{duracion_min}{duracion_seg}")
    duraciont=duracion
    #complemento
    complemento="VENTA_ONE-CONTACT-MEDELLIN_TMK_CONVERGENTE_TMK"
    #hora y fecha
    hora=ora[0:2]+"-"+ora[2:4]+"-"+ora[4:6]
    fecha = numero[6:8] + "-" + numero[4:6] + "-" + numero[0:4]
    nuevo_nombre=f"{fecha}_{hora}_{duracion}_{cel}_{cedu}_{complemento}_{campaña}{extencion}"
    ruta_archivo_despues=f"{carpeta_cargue}{nuevo_nombre}"
    #renombrar
    os.rename(ruta_archivo_antes ,ruta_archivo_despues)
    # enviar a carpeta exporte
    ruta_archivo_destino = os.path.join(carpeta_destino, nuevo_nombre)
    shutil.move(ruta_archivo_despues, ruta_archivo_destino)

def no_venta(archivo, duracion):

    nombre_llamada =archivo.split("/")
    nombre_llamada = nombre_llamada[-1]

    ruta_archivo_antes=os.path.join(carpeta_cargue, archivo)


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
    #duraciont=(f"{duracion_min}{duracion_seg}")
    duraciont=duracion
    #complemento
    complemento="NO_VENTA_ONE-CONTACT-MEDELLIN_TMK_CONVERGENTE_TMK"
    #hora y fecha
    hora=ora[0:2]+"-"+ora[2:4]+"-"+ora[4:6]
    fecha = numero[6:8] + "-" + numero[4:6] + "-" + numero[0:4]
    nuevo_nombre=f"{fecha}_{hora}_{duracion}_{cel}_{cedu}_{complemento}_{campaña}{extencion}"
    ruta_archivo_despues=f"{carpeta_cargue}{nuevo_nombre}"
    #renombrar
    os.rename(ruta_archivo_antes,ruta_archivo_despues)
    # enviar a carpeta exporte
    ruta_archivo_destino = os.path.join(carpeta_destino, nuevo_nombre)
    shutil.move(ruta_archivo_despues, ruta_archivo_destino)
    
    
