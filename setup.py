from cx_Freeze import setup, Executable

# Configuración del ejecutable
setup(
    name="Ejecutable",
    version="1.0",
    description="Reproductor OneContact",
    executables=[Executable("interfaz.py", icon="icono.ico")]
)