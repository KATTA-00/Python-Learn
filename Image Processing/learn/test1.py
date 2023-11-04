import subprocess
import venv
import platform  # Import the platform module

# Define the virtual environment path
venv_path = ".\env"

# Create the virtual environment
venv.create(venv_path, with_pip=True)

# Activate the virtual environment
activate_script = venv_path + "\Scripts\activate" if platform.system() == "Windows" else venv_path + "/bin/activate"
subprocess.run(activate_script, shell=True, check=True)

# Install packages using pip
packages_to_install = ["numpy"]
for package in packages_to_install:
    subprocess.run(f"pip install {package}", shell=True, check=True)

