import os, sys

moduleFolder = os.getcwd() + '\TMRemote\Scripts'
if os.path.isdir(moduleFolder):
	if not moduleFolder in sys.path:
		sys.path.append(moduleFolder)
	try:
		from TMRLogger import Log
		Log().main()
	except ImportError as error:
		print('> Could not find TMRLogger inside {}, please place it there and restart client.'.format(moduleFolder))
else:
	os.mkdir(moduleFolder)
	print('> Created {}, please place TMRLogger.pyc in this folder.'.format(moduleFolder))
