from cx_Freeze import setup, Executable

# Configuración del ejecutable
setup(
    name="Ejecutable",
    version="1.0",
    description="Descripción",
    executables=[Executable("interfaz.py")]
)