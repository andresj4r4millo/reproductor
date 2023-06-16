from cx_Freeze import setup, Executable

# Configuración del ejecutable
setup(
    name="Reproductor",
    version="1.1",
    description="Reproductor OneContact",
    executables=[Executable("interfaz.py", icon="icono.ico")]
)