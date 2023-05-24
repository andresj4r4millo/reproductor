import sched
import time

def establecer_intervalo(funcion, segundos):
    scheduler = sched.scheduler(time.time, time.sleep)
    while True:
        funcion()
        scheduler.enter(segundos, 1, establecer_intervalo, (segundos,))  # Programar la siguiente ejecución
        scheduler.run()

def cronometro(tiempo): #tiempo en segundos
    for segundos in range(tiempo):
        minutos, segundos = divmod(segundos, 60)
        horas, minutos = divmod(minutos, 60)
        tiempo_formateado = "{:02d}:{:02d}:{:02d}".format(horas, minutos, segundos)
        time.sleep(1)
        return tiempo_formateado