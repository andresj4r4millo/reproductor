# Reproductor de Musica

# importacion de librerias
from tkinter import Button, Label, Tk, filedialog, ttk, Frame, PhotoImage
import pygame
import random
import mutagen
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from logica import venta, no_venta
import os
carpeta_cargue = 'carpeta_cargue/'
# from mutagen.mp3 import MP3
# pygame.mixer.pre_init(frequency=44100)

pygame.mixer.init()
pygame.mixer.init(frequency=44100)
llamada_actual = ""
archivos = ""
duracion = ""


# comandos - funciones


def obtener_tiempo_actual():
	segundos_totales = pygame.mixer.music.get_pos() // 1000
	minutos = segundos_totales // 60
	segundos = segundos_totales % 60
	return minutos, segundos


def actualizar_etiqueta(etiqueta):
	minutos, segundos = obtener_tiempo_actual()
	etiqueta.config(text=f"{minutos:02d}:{segundos:02d}")
	etiqueta.after(1000, lambda: actualizar_etiqueta(etiqueta))


def inicializacion():
	global llamada_actual, pos, carpeta_cargue
	global archivos
	pos = 0
	archivos = os.listdir(carpeta_cargue)
	for archivo in archivos:
		if archivo.endswith(".mp3"):
			llamada_actual = f"{carpeta_cargue}{archivo}"
			print(f"llamada_actual: {llamada_actual}")

	# iniciar reproduccion automaticamente luego de abrir los archivos
	pygame.mixer.music.load(llamada_actual)
	pygame.mixer.music.play()
	actualizar_etiqueta(tiempo_transcurrido)
	iniciar_reproduccion()


lista = []
for i in range(50, 200, 10):
	lista.append(i)


def iniciar_reproduccion():
	global llamada_actual, pos, n, actualizar, archivos
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

	time = pygame.mixer.music.get_pos()
	x = int(int(time) * 0.001)
	tiempo["value"] = x  # posicion de la llamada

	y = 0.5
	pygame.mixer.music.set_volume(y)

	audio = mutagen.File(f"{carpeta_cargue}{llamada_actual}") 
	log = audio.info.length
	minutos, segundos = divmod(log, 60)

	minutos, segundos = int(minutos), int(segundos)
	tt = minutos * 60 + segundos

	tiempo["maximum"] = tt  # tiempo total de la llamada

	segundos = str(segundos).rjust(2, "0")

	tiempo_total["text"] = str(minutos) + ":" + str(segundos)
	global duracion
	duracion = tiempo_total["text"]

	actualizar = ventana.after(100, iniciar_reproduccion)

	if x == tt:
		ventana.after_cancel(actualizar)
		tiempo_total["text"] = "00:00"
		detener_efecto()
		if pos != n:
			pos = pos + 1
			ventana.after(100, iniciar_reproduccion)
			# pygame.mixer.music.play()
			# actualizar_etiqueta(tiempo_transcurrido)
		if pos == n:
			pos = 0


def iniciar():
	pygame.mixer.music.unpause()


def adelantar():
	current_position = (
		pygame.mixer.music.get_pos() // 1000
	)  # Get current position in seconds
	new_position = current_position + 5  # Forward by 5 seconds
	pygame.mixer.music.set_pos(new_position)  # Set the new position
	return
	tiempo = pygame.mixer.music.get_pos()
	tiempo /= 1000
	tiempo = round(tiempo, 0)
	tiempo += 5
	tiempo = int(tiempo)
	print(tiempo)
	pygame.mixer.music.rewind()
	pygame.mixer.music.set_pos(tiempo)


def atrasar():
	global pos, n
	if pos == n - 1:
		pos = 0
	else:
		pos = pos + 1
	cantidad["text"] = str(pos) + "/" + str(n)


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
	global actualizar
	pygame.mixer.music.stop()
	ventana.after_cancel(actualizar)
	detener_efecto()


def pausa():
	global actualizar
	pygame.mixer.music.pause()
	ventana.after_cancel(actualizar)
	detener_efecto()


def continuar():
	pygame.mixer.music.unpause()
	ventana.after(100, iniciar_reproduccion)

def fun_venta():
	global llamada_actual, duracion
	pausa()
	venta(llamada_actual, duracion)

def fun_no_venta():
	global llamada_actual, duracion
	pausa()
	no_venta(llamada_actual, duracion)

"""def modificar_tiempo_transcurrido(segundos):
	for segundos in range(segundos):
		minutos, segundos = divmod(segundos, 60)
		horas, minutos = divmod(minutos, 60)
		tiempo_formateado = "{:02d}:{:02d}:{:02d}".format(horas, minutos, segundos)
		tiempo_transcurrido["text"] = tiempo_formateado
		time.sleep(1)"""


ventana = Tk()
ventana.title("Reproductor de Musica")
ventana.iconbitmap("icono.ico")
ventana.config(bg="black")
ventana.resizable(0, 0)

estilo = ttk.Style()
estilo.theme_use("clam")
estilo.configure(
	"Vertical.TProgressbar",
	foreground="green2",
	background="green2",
	troughcolor="black",
	bordercolor="black",
	lightcolor="green2",
	darkcolor="green2",
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
	troughcolor="DarkOrchid1",
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

tiempo_transcurrido = Label(frame2, bg="black", fg="green2", width=5)
tiempo_transcurrido.grid(row=0, column=7)

tiempo_total = Label(frame2, bg="black", fg="green2", width=5)
tiempo_total.grid(row=0, column=8)

nombre = Label(frame2, bg="black", fg="red", width=55)
nombre.grid(column=0, row=1, columnspan=8, padx=5)
cantidad = Label(frame2, bg="black", fg="green2")
cantidad.grid(column=8, row=1)

# iconos
imagen1 = PhotoImage(file="carpeta.png")
imagen2 = PhotoImage(file="play.png")
imagen3 = PhotoImage(file="pausa.png")
imagen4 = PhotoImage(file="repetir.png")
imagen5 = PhotoImage(file="stop.png")
imagen6 = PhotoImage(file="anterior.png")
imagen7 = PhotoImage(file="adelante.png")
imagen8 = PhotoImage(file="atras.png")

# botones
boton2 = Button(frame2, image=imagen2, bg="yellow", command=iniciar)
boton2.grid(column=1, row=2, pady=10)
boton3 = Button(frame2, image=imagen3, bg="red", command=pausa)
boton3.grid(column=2, row=2, pady=10)
venta = Button(
	frame2,
	text="VENTA",
	bg="red",
	#command=lambda: [pausa, venta(llamada_actual, duracion)],
	command= fun_venta
)


venta.grid(column=3, row=2, pady=10)
no_venta = Button(
	frame2,
	text="NO VENTA",
	bg="red",
	command=fun_no_venta
)
no_venta.grid(column=4, row=2, pady=10)

atras = Button(frame2, image=imagen8, bg="green", command=atrasar)
atras.grid(column=5, row=2, pady=10)

adelante = Button(frame2, image=imagen7, bg="green", command=adelantar)
adelante.grid(column=6, row=2, pady=10)

# Obtener el objeto de volumen del dispositivo de reproducción predeterminado
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Obtener el rango de volumen
volume_range = volume.GetVolumeRange()

# Establecer el volumen (0.0 - 1.0)
new_volume = 0.9  # se reprroduce al 90% del volumen
volume.SetMasterVolumeLevel(
	volume_range[0] + (volume_range[1] - volume_range[0]) * new_volume, None
)

inicializacion()
ventana.mainloop()