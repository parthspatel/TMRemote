from cx_Freeze import Executable, setup

base = 'Win32GUI'

include_files = ['./icons']
packages = ['idna', 'backend']

options = {
    'build_exe': {
        'packages': packages,
  		'include_files': include_files
    },
}

executables = [Executable("TMRemote.py",
                          base=base,
                          icon=r'icons/icon.ico')]

setup(
    name="TMRemote",
    options=options,
    version="1.0.0.0",
    description='Terminal Manager Remote',
    executables=executables
)
