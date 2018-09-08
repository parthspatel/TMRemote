from cx_Freeze import Executable, setup
import os
base = 'Win32GUI'

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

include_files = ['./icons']

packages = ['idna', 'zipfile']

options = {
    'build_exe': {
        'packages': packages,
  		'include_files': include_files
    },
}

executables = [Executable("TMRInstaller.py",
                          base=base,
                          icon=r'icons\icon.ico')]

setup(
    name="TMRInstaller",
    options=options,
    version="1.0.0.0",
    description='TMRemote Installer',
    executables=executables
)
