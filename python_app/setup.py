from cx_Freeze import Executable, setup

base = 'Win32GUI'

packages = ["idna"]
options = {
    'build_exe': {
        'packages': packages,
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
