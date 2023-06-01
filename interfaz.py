# ---------------------------------------------- IMPORTACION DE LIBRERIAS ----------------------------------------------
from tkinter import Button, Label, Tk, ttk, Frame, PhotoImage
import random
import mutagen
from logica import venta, mover, no_venta
import os
import time
import vlc

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

def reproducir_rapidamente():
    reproductor.set_rate(1.5)

def reproducir_normalmente():
    reproductor.set_rate(1)

def actualizar_etiqueta_tiempo_llamada():
    global actualizar_tiempo_llamada
    transcurrido = reproductor.get_time() / 1000
    minutos, segundos = divmod(transcurrido, 60)
    tiempo_transcurrido.config(text=f"{int(minutos):02d}:{int(segundos):02d}")
    actualizar_tiempo_llamada = tiempo_transcurrido.after(1000, actualizar_etiqueta_tiempo_llamada)

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
    #reproductor.get_instance()
    iniciar_reproduccion()
    actualizar_etiqueta_tiempo_llamada()


lista = []
for i in range(50, 200, 10):
    lista.append(i)

def iniciar_reproduccion():
    global llamada_actual, pos, n, actualizar_barras, archivos, log, reproductor, stime, actualizar_tiempo_llamada

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

    llamada_actual = archivos[pos]

    nombre_llamada = llamada_actual.split("/")
    nombre_llamada = nombre_llamada[-1]
    nombre["text"] = nombre_llamada

    time = reproductor.get_time()
    x = int(int(time) * 0.001)
    tiempo["value"] = x  # posicion de la llamada

    audio = mutagen.File(f"{carpeta_cargue}/{llamada_actual}")
    log = audio.info.length
    minutos, segundos = divmod(log, 60)

    minutos, segundos = int(minutos), int(segundos)
    tt = minutos * 60 + segundos

    tiempo["maximum"] = tt  # tiempo total de la llamada

    segundos = str(segundos).rjust(2, "0")

    tiempo_total["text"] = str(minutos) + ":" + str(segundos)
    global duracion
    duracion = tiempo_total["text"]

    actualizar_barras = ventana.after(100, iniciar_reproduccion)

def reanudar():
    global reproductor
    reproductor.play()
    actualizar_etiqueta_tiempo_llamada()
    ventana.after(100, iniciar_reproduccion)

def adelantar():
    transcurrido = reproductor.get_time()
    nuevo_tiempo = transcurrido + 5000
    reproductor.set_time(nuevo_tiempo)

def atrasar():
    transcurrido = reproductor.get_time()
    nuevo_tiempo = transcurrido - 5000
    reproductor.set_time(nuevo_tiempo)

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
    reproductor.pause()
    ventana.after_cancel(actualizar_barras)
    tiempo_transcurrido.after_cancel(actualizar_tiempo_llamada)
    detener_efecto()

def fun_venta():
    global  archivos, carpeta_cargue
    stop()
    venta( archivos,carpeta_cargue)
    llamadas=os.listdir(carpeta_cargue)
    mover(llamadas)
    archivos.pop(0)
    llamadas.pop(0)
    inicializacion()

def fun_no_venta():
    global  archivos, carpeta_cargue
    stop()
    no_venta(archivos,carpeta_cargue)
    llamadas=os.listdir(carpeta_cargue)
    mover(llamadas)
    archivos.pop(0)
    llamadas.pop(0)
    inicializacion()

# ---------------------------------------------- MAQUETACION ----------------------------------------------
ventana = Tk()
ventana.title("Reproductor de Musica")
ventana.iconbitmap("iconos/icono.ico")
ventana.config(bg="black")
ventana.resizable(0, 0)

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

nombre = Label(frame2, bg="black", fg="red", width=55)
nombre.grid(column=0, row=1, columnspan=8, padx=5)
cantidad = Label(frame2, bg="black", fg="green2")
cantidad.grid(column=8, row=1)

# iconos
imagen2 = PhotoImage(file="iconos/play.png")
imagen3 = PhotoImage(file="iconos/pausa.png")
imagen7 = PhotoImage(file="iconos/adelante.png")
imagen8 = PhotoImage(file="iconos/atras.png")
imagen9 = PhotoImage(file="iconos/venta.png")
imagen10 = PhotoImage(file="iconos/no_venta.png")
imagen11 = PhotoImage(file="iconos/rapida.png")
imagen12 = PhotoImage(file="iconos/normal.png")

# btn iniciar
boton2 = Button(frame2, image=imagen2, bg="#1d50aa", command=reanudar)
boton2.grid(column=0, row=2, pady=10, sticky="ew")

# btn pausar
boton3 = Button(frame2, image=imagen3, bg="#1d50aa", command=pausar)
boton3.grid(column=1, row=2, pady=10, sticky="ew")

# btn venta
boton_venta = Button(
    frame2,
    image=imagen9,
    bg="#1d50aa",
    command=fun_venta
)
boton_venta.grid(column=2, row=2, pady=10, sticky="ew")

# no venta
boton_no_venta = Button(frame2, image=imagen10, bg="#1d50aa", command=fun_no_venta)
boton_no_venta.grid(column=3, row=2, pady=10, sticky="ew")

# btn atras
atras = Button(frame2, image=imagen8, bg="#1d50aa", command=atrasar)
atras.grid(column=4, row=2, pady=10, sticky="ew")

# btn adelantar
adelante = Button(frame2, image=imagen7, bg="#1d50aa", command=adelantar)
adelante.grid(column=5, row=2, pady=10, sticky="ew")

reproduccion_normal = Button(frame2, image=imagen12, bg="#1d50aa", command=reproducir_normalmente)
reproduccion_normal.grid(column=6, row=2, pady=10, sticky="ew")

reproduccion_rapida = Button(frame2, image=imagen11, bg="#1d50aa", command=reproducir_rapidamente)
reproduccion_rapida.grid(column=7, row=2, pady=10, columnspan=2, sticky="ew")

inicializacion()
ventana.mainloop()