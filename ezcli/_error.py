'''Module holding the EzCLIError and EzCLIWarning classes'''
import warnings

class EzCLIError (Exception):
	'''Exception raised when the user use ezCLI the wrong way'''

class EzCLIWarning (Warning):
	'''Warning about ezCLI'''

def warn(message):
	warnings.warn(message, EzCLIWarning, stacklevel=2)