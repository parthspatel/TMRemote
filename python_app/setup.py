from cx_Freeze import Executable, setup

base = 'Win32GUI'

includefiles = ['README.txt', 'CHANGELOG.txt', 'helpers\uncompress\unRAR.exe', , 'helpers\uncompress\unzip.exe']
packages = ["idna"]

options = {
    'build_exe': {
        'packages': packages,
  		'include_files': includefiles
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
