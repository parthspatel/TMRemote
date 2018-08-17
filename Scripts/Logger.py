try:
	import TMRLogger
	TMRLogger.Log().main()
except ModuleNotFoundError:
	print('> Could not find TMRLogger inside Appdata folder, please place it there and restart client.')