# ---------------------------------------------- IMPORTACION DE LIBRERIAS ----------------------------------------------
from tkinter import Button, Label, Tk, ttk, Frame, PhotoImage, messagebox
import random
import mutagen
from logica import venta, mover, no_venta
import os
import time
import vlc
from pynput import keyboard
from conversor import convertir_llamadas

# ---------------------------------------------- INICIALIZACION DE VARIABLES ----------------------------------------------
carpeta_cargue = 'carpeta_cargue'
carpeta_destino='carpeta_destino'
stime = None
reproductor = None
actualizar_barras = None
actualizar_tiempo_llamada = None
llamada_actual = ""
archivos = ""
duracion = ""

# ---------------------------------------------- FUNCIONES ----------------------------------------------

def mostrar_ventana_modal():
    # Crear la ventana modal
    # Mostrar un mensaje en la ventana modal
    mensaje = "Convirtiendo archivos gsm a mp3. Espera por favor."
    messagebox.showinfo("Mensaje", mensaje)



# Funciones de teclado 
# para adelantar y atrasar la llamada 30 segundos y para pausar y reanudarla
# def on_key(event):
#     print(event)
#     if event.name == "flecha izquierda":
#         atrasar(30000)
#     elif event.name == "flecha derecha":
#         adelantar(30000)
#     elif event.name == "space":
#         if reproductor.is_playing():
#             pausar()
#         else:
#             reanudar()
# keyboard.hook(on_key)

def key_pressed(event):
    if event.widget.focus_get() == event.widget:
        if event.keysym == "Left":
            atrasar(30000)
        elif event.keysym == "Right":
         adelantar(30000)
        elif event.keysym == "space":
            if reproductor.is_playing():
             pausar()
            else:
             reanudar()


#función que se ejecuta cuando se presiona el botón de "no aplica"
def fun_no_aplica():
    global  carpeta_cargue
    stop()
    llamadas=os.listdir(carpeta_cargue)
    mover(llamadas, "no_aplica")
    archivos.pop(0)
    llamadas.pop(0)
    inicializacion()

def reproducir_rapidamente():
    reproductor.set_rate(1.5)

def reproducir_normalmente():
    reproductor.set_rate(1)

#función que se  encarga de actualizar el segundo actual de la llamada
def funcion_actualizar_tiempo():
    global actualizar_tiempo_llamada
    transcurrido = reproductor.get_time()
    minutos, segundos = divmod(transcurrido / 1000, 60)
    tiempo_transcurrido.config(text=f"{int(minutos):02d}:{int(segundos):02d}")

    #actualizar barra de tiempo horizontal    
    x = int(int(transcurrido) * 0.001)
    tiempo["value"] = x  # posicion de la llamada

    actualizar_tiempo_llamada = tiempo_transcurrido.after(1000, funcion_actualizar_tiempo)

#selecciona la primera llamada de la carpeta de cargue y la reproduce
def inicializacion():
    global llamada_actual, pos, carpeta_cargue, reproductor, archivos, archivo, stime
    pos = 0

    archivos = os.listdir(carpeta_cargue)

    try:
        archivo=archivos[0]
    except:
        ventana.destroy()

        
    if archivo.endswith(".mp3"):
        llamada_actual = archivo

    reproductor = vlc.MediaPlayer(f"file:///carpeta_cargue/{llamada_actual}")
    reproductor.play()
    stime = time.time()
    iniciar_reproduccion()
    funcion_actualizar_tiempo()


lista = []
for i in range(50, 200, 10):
    lista.append(i)

#define el nombre de la llamada y el tiempo total de la llamada para mostrarlo en la interfaz 
def iniciar_reproduccion():
    global llamada_actual, pos, n, archivos, log, reproductor, stime, actualizar_tiempo_llamada, duracion

    llamada_actual = archivos[pos]

    nombre_llamada = llamada_actual.split("/")
    nombre_llamada = nombre_llamada[-1]
    nombre["text"] = nombre_llamada

    audio = mutagen.File(f"{carpeta_cargue}/{llamada_actual}")
    log = audio.info.length
    minutos, segundos = divmod(log, 60)

    minutos, segundos = int(minutos), int(segundos)
    tt = minutos * 60 + segundos

    tiempo["maximum"] = tt  # tiempo total de la llamada

    segundos = str(segundos).rjust(2, "0")

    tiempo_total["text"] = str(minutos) + ":" + str(segundos)
    duracion = tiempo_total["text"]

    funcion_actualizar_barras()

#se encarga de renderizar la animación de las barras cuando una llamada se está reproduciendo
def funcion_actualizar_barras():
    global actualizar_barras

    if reproductor.is_playing():
        barra1["value"] = random.choice(lista)
        barra2["value"] = random.choice(lista)
        barra3["value"] = random.choice(lista)
        barra4["value"] = random.choice(lista)
        barra5["value"] = random.choice(lista)
        barra6["value"] = random.choice(lista)
        barra7["value"] = random.choice(lista)
        barra8["value"] = random.choice(lista)
        barra9["value"] = random.choice(lista)
        barra10["value"] = random.choice(lista)
        barra11["value"] = random.choice(lista)
        barra12["value"] = random.choice(lista)
        barra13["value"] = random.choice(lista)
        barra14["value"] = random.choice(lista)
        barra15["value"] = random.choice(lista)
        barra16["value"] = random.choice(lista)
        barra17["value"] = random.choice(lista)
        barra18["value"] = random.choice(lista)
        barra19["value"] = random.choice(lista)
        barra20["value"] = random.choice(lista)
    else:
        detener_efecto()
    
    actualizar_barras = ventana.after(100, funcion_actualizar_barras)

#reanuda la reproduccion
def reanudar():
    if reproductor.is_playing():
        return
     
    global actualizar_barras

    if reproductor.get_state() == vlc.State.Ended:
        ventana.after_cancel(actualizar_barras)
        reproductor.stop()
        reproductor.play()
        funcion_actualizar_tiempo()
        ventana.after(100, funcion_actualizar_barras)
        return

    reproductor.play()
    funcion_actualizar_tiempo()
    ventana.after(100, funcion_actualizar_barras)

def adelantar(milisegundos = 5000):
    if reproductor.is_playing():
        transcurrido = reproductor.get_time()
        nuevo_tiempo = transcurrido + milisegundos
        reproductor.set_time(nuevo_tiempo)

def atrasar(milisegundos = 5000):
    if reproductor.is_playing():
        transcurrido = reproductor.get_time()
        nuevo_tiempo = transcurrido - milisegundos
        reproductor.set_time(nuevo_tiempo)

#detiene la animación de las barras
def detener_efecto():
    barra1["value"] = 50
    barra2["value"] = 60
    barra3["value"] = 70
    barra4["value"] = 80
    barra5["value"] = 90
    barra6["value"] = 100
    barra7["value"] = 90
    barra8["value"] = 80
    barra9["value"] = 70
    barra10["value"] = 60
    barra11["value"] = 60
    barra12["value"] = 70
    barra13["value"] = 80
    barra14["value"] = 90
    barra15["value"] = 100
    barra16["value"] = 90
    barra17["value"] = 80
    barra18["value"] = 70
    barra19["value"] = 60
    barra20["value"] = 50

def stop():
    global actualizar_barras
    reproductor.stop()
    ventana.after_cancel(actualizar_barras)
    detener_efecto()

def pausar():
    global actualizar_barras, reproductor, actualizar_tiempo_llamada
    
    if reproductor.is_playing():
        reproductor.pause()
        ventana.after_cancel(actualizar_barras)
        tiempo_transcurrido.after_cancel(actualizar_tiempo_llamada)
        detener_efecto()

#se ejecuta cuando se presiona el botón que clasifica una llamada como venta
def fun_venta():
    global  archivos, carpeta_cargue
    stop()
    venta( archivos,carpeta_cargue)
    llamadas=os.listdir(carpeta_cargue)
    mover(llamadas)
    archivos.pop(0)
    llamadas.pop(0)
    inicializacion()

#se ejecuta cuando se presiona el botón que clasifica una llamada como "no venta"
def fun_no_venta():
    global  archivos, carpeta_cargue
    stop()
    no_venta(archivos,carpeta_cargue)
    llamadas=os.listdir(carpeta_cargue)
    mover(llamadas)
    archivos.pop(0)
    llamadas.pop(0)
    inicializacion()

# ---------------------------------------------- DISEÑO DE INTERFAZ ----------------------------------------------
ventana = Tk()
ventana.title("Reproductor de Musica")
ventana.iconbitmap("iconos/icono.ico")
ventana.config(bg="black")
ventana.resizable(0, 0)
ventana.bind("<Key>", key_pressed)


estilo = ttk.Style()
estilo.theme_use("clam")
estilo.configure(
    "Vertical.TProgressbar",
    foreground="#f88521",
    background="#f88521",
    troughcolor="black",
    bordercolor="black",
    lightcolor="#f88521",
    darkcolor="#f88521",
)

frame1 = Frame(ventana, bg="black", width=600, height=350)
frame1.grid(column=0, row=0, sticky="nsew")
frame2 = Frame(ventana, bg="black", width=600, height=50)
frame2.grid(column=0, row=1, sticky="nsew")

#barras para la animación de reproducción
barra1 = ttk.Progressbar(
    frame1, orient="vertical", length=300, maximum=300, style="Vertical.TProgressbar"
)  # ,takefocus=True mode='determinate',
barra1.grid(column=0, row=0, padx=1)
barra2 = ttk.Progressbar(
    frame1, orient="vertical", length=300, maximum=300, style="Vertical.TProgressbar"
)
barra2.grid(column=1, row=0, padx=1)
barra3 = ttk.Progressbar(
    frame1, orient="vertical", length=300, maximum=300, style="Vertical.TProgressbar"
)
barra3.grid(column=2, row=0, padx=1)
barra4 = ttk.Progressbar(
    frame1, orient="vertical", length=300, maximum=300, style="Vertical.TProgressbar"
)
barra4.grid(column=3, row=0, padx=1)
barra5 = ttk.Progressbar(
    frame1, orient="vertical", length=300, maximum=300, style="Vertical.TProgressbar"
)
barra5.grid(column=4, row=0, padx=1)
barra6 = ttk.Progressbar(
    frame1, orient="vertical", length=300, maximum=300, style="Vertical.TProgressbar"
)
barra6.grid(column=5, row=0, padx=1)
barra7 = ttk.Progressbar(
    frame1, orient="vertical", length=300, maximum=300, style="Vertical.TProgressbar"
)  # ,takefocus=True
barra7.grid(column=6, row=0, padx=1)
barra8 = ttk.Progressbar(
    frame1, orient="vertical", length=300, maximum=300, style="Vertical.TProgressbar"
)
barra8.grid(column=7, row=0, padx=1)
barra9 = ttk.Progressbar(
    frame1, orient="vertical", length=300, maximum=300, style="Vertical.TProgressbar"
)
barra9.grid(column=8, row=0, padx=1)
barra10 = ttk.Progressbar(
    frame1, orient="vertical", length=300, maximum=300, style="Vertical.TProgressbar"
)
barra10.grid(column=9, row=0, padx=1)
barra11 = ttk.Progressbar(
    frame1, orient="vertical", length=300, maximum=300, style="Vertical.TProgressbar"
)
barra11.grid(column=10, row=0, padx=1)
barra12 = ttk.Progressbar(
    frame1, orient="vertical", length=300, maximum=300, style="Vertical.TProgressbar"
)
barra12.grid(column=11, row=0, padx=1)
barra13 = ttk.Progressbar(
    frame1, orient="vertical", length=300, maximum=300, style="Vertical.TProgressbar"
)
barra13.grid(column=12, row=0, padx=1)
barra14 = ttk.Progressbar(
    frame1, orient="vertical", length=300, maximum=300, style="Vertical.TProgressbar"
)
barra14.grid(column=13, row=0, padx=1)
barra15 = ttk.Progressbar(
    frame1, orient="vertical", length=300, maximum=300, style="Vertical.TProgressbar"
)
barra15.grid(column=14, row=0, padx=1)
barra16 = ttk.Progressbar(
    frame1, orient="vertical", length=300, maximum=300, style="Vertical.TProgressbar"
)
barra16.grid(column=15, row=0, padx=1)
barra17 = ttk.Progressbar(
    frame1, orient="vertical", length=300, maximum=300, style="Vertical.TProgressbar"
)
barra17.grid(column=16, row=0, padx=1)
barra18 = ttk.Progressbar(
    frame1, orient="vertical", length=300, maximum=300, style="Vertical.TProgressbar"
)
barra18.grid(column=17, row=0, padx=1)
barra19 = ttk.Progressbar(
    frame1, orient="vertical", length=300, maximum=300, style="Vertical.TProgressbar"
)
barra19.grid(column=18, row=0, padx=1)
barra20 = ttk.Progressbar(
    frame1, orient="vertical", length=300, maximum=300, style="Vertical.TProgressbar"
)
barra20.grid(column=19, row=0, padx=1)

#estilos de la barra de progreso horizontal
estilo1 = ttk.Style()
estilo1.theme_use("clam")
estilo1.configure(
    "Horizontal.TProgressbar",
    foreground="red",
    background="black",
    troughcolor="#1d50aa", #azul
    bordercolor="#970BD9",
    lightcolor="#970BD9",
    darkcolor="black",
)

tiempo = ttk.Progressbar(
    frame2,
    orient="horizontal",
    length=390,
    mode="determinate",
    style="Horizontal.TProgressbar",
)

tiempo.grid(row=0, columnspan=7, padx=5)

tiempo_transcurrido = Label(frame2, bg="black", fg="orange", width=5)
tiempo_transcurrido.grid(row=0, column=7)

tiempo_total = Label(frame2, bg="black", fg="orange", width=5)
tiempo_total.grid(row=0, column=8)

#elemento que muestra el nombre de la llamada
nombre = Label(frame2, bg="black", fg="red", width=55)
nombre.grid(column=0, row=1, columnspan=8, padx=5)
cantidad = Label(frame2, bg="black", fg="green2")
cantidad.grid(column=8, row=1)

# iconos de la interfaz
imagen2 = PhotoImage(file="iconos/play.png")
imagen3 = PhotoImage(file="iconos/pausa.png")
imagen7 = PhotoImage(file="iconos/adelante.png")
imagen8 = PhotoImage(file="iconos/atras.png")
imagen9 = PhotoImage(file="iconos/venta.png")
imagen10 = PhotoImage(file="iconos/no_venta.png")
imagen11 = PhotoImage(file="iconos/rapida.png")
imagen12 = PhotoImage(file="iconos/normal.png")
imagen13 = PhotoImage(file="iconos/no_aplica.png")

# botón iniciar
boton2 = Button(frame2, image=imagen2, bg="#1d50aa", command=reanudar)
boton2.grid(column=0, row=2, pady=10, sticky="ew")

# botón pausar
boton3 = Button(frame2, image=imagen3, bg="#1d50aa", command=pausar)
boton3.grid(column=1, row=2, pady=10, sticky="ew")

# botón venta
boton_venta = Button(
    frame2,
    image=imagen9,
    bg="#1d50aa",
    command=fun_venta
)
boton_venta.grid(column=2, row=2, pady=10, sticky="ew")

# botón no aplica
boton_venta = Button(
    frame2,
    image=imagen13,
    bg="#1d50aa",
    command=fun_no_aplica
)
boton_venta.grid(column=3, row=2, pady=10, sticky="ew")

# no venta
boton_no_venta = Button(frame2, image=imagen10, bg="#1d50aa", command=fun_no_venta)
boton_no_venta.grid(column=4, row=2, pady=10, sticky="ew")

# botón atras
atras = Button(frame2, image=imagen8, bg="#1d50aa", command=atrasar)
atras.grid(column=5, row=2, pady=10, sticky="ew")

# botón adelantar
adelante = Button(frame2, image=imagen7, bg="#1d50aa", command=adelantar)
adelante.grid(column=6, row=2, pady=10, sticky="ew")

#botón de reproducción normal o velocidad estandar
reproduccion_normal = Button(frame2, image=imagen12, bg="#1d50aa", command=reproducir_normalmente)
reproduccion_normal.grid(column=7, row=2, pady=10, sticky="ew")

#botón de reproducción rápida
reproduccion_rapida = Button(frame2, image=imagen11, bg="#1d50aa", command=reproducir_rapidamente)
reproduccion_rapida.grid(column=8, row=2, pady=10, sticky="ew")

mostrar_ventana_modal()
convertir_llamadas()
inicializacion()

#muestra la interfaz del reproductor
ventana.mainloop()