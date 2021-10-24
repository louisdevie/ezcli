'''Module holding the EzCLIError and EzCLIWarning classes'''

class EzCLIError (Exception):
	'''Exception raised when the user use ezCLI the wrong way'''

class EzCLIWarning (Warning):
	'''Warning about ezCLI'''