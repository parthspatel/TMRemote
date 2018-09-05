import os, sys

class versionCheck():
	def __init__(self):
		self.version = '0.1.1'

moduleFolder = os.getcwd() + '\TMRemote\Scripts'
if os.path.isdir(moduleFolder):
	if not moduleFolder in sys.path:
		sys.path.append(moduleFolder)
	try:
		from TMRLogger import Log
		Log().main()
	except ImportError as error:
		pass
else:
	os.mkdir(moduleFolder)
