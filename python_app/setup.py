from cx_Freeze import Executable, setup

base = 'Win32GUI'

includes = []
packages = ['idna', 'backend']

options = {
    'build_exe': {
        'packages': packages,
  		'includes': includes
    },
}

executables = [Executable("TMRemote.py",
                          base=base,
                          icon=r'resources/icon.ico')]

setup(
    name="TMRemote",
    options=options,
    version="1.0.0.0",
    description='Terminal Manager Remote',
    executables=executables
)
