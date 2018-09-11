import os, sys, GameState

class versionCheck():
	def __init__(self):
		self.version = '0.1.1'

moduleFolder = os.getcwd() + '\TMRemote\Scripts'
if os.path.isdir(moduleFolder):
	if not moduleFolder in sys.path:
		sys.path.append(moduleFolder)
	try:
		from TMRLogger import Log
		if GameState.IsInGame():
			Log().main()
	except ImportError as error:
		pass
