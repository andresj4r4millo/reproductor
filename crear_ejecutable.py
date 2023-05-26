from cx_Freeze import setup, Executable

# Specify the path to your Python script
script = 'conversor.py'

# Define the base
base = None
# Use 'Win32GUI' if your script is a GUI application on Windows

# Define the executables
executables = [Executable(script, base=base)]

# Set the options
options = {
    'build_exe': {
        'include_files': [],  # Add any additional files or data required by your script
        'excludes': [],  # Add any modules/packages to be excluded
    }
}

# Create the setup
setup(
    name='YourScript',
    version='1.0',
    description='Description of your script',
    options=options,
    executables=executables
)
