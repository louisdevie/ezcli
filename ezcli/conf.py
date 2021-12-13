'''Holds the configuration of the app'''
__all__ = ['config']


from ._error import EzCLIError, warn



# configuration singleton
class Configuration:
	NAME = '[application name]'
	VERSION = '[unknown]'
	LANGUAGE = 'en'
	ISDONE = False

	def done(self):
		self.ISDONE = True

	def set_name(self, name):
		if isinstance(name, str):
			self.NAME = name
		else:
			raise TypeError(f'The application\'s name must be a string, not a {type(name)}')

	def set_version(self, ver):
		if isinstance(ver, str):
			self.VERSION = ver
		else:
			raise TypeError(f'The application\'s version must be a string, not a {type(ver)}')

	def set_language(self, lang):
		self.LANGUAGE = lang

CONFIG = Configuration()



def config(appname=None, appversion=None, language='en'):
	'''Configure ezCLI.
It can be called only once.'''

	# Prevents the user from re-configuring his app
	if CONFIG.ISDONE:
		raise EzCLIError('ezCLI is already configured')

	# the import is done inside the function to prevent a circular import
	from . import _prebuilt

	# Set the app's name
	if appname is None:
		CONFIG.set_name(_prebuilt.NO_NAME)
	else:
		CONFIG.set_name(appname)

	# Set the app's version
	if appversion is None:
		CONFIG.set_version(_prebuilt.NO_VERSION)
	else:
		CONFIG.set_version(appversion)

	# Set the app's language
	if language in _prebuilt.available:
		CONFIG.set_language(language)
		if language in _prebuilt.incomplete:
			warn('the language [{language}] isn\'t fully supported') 
	else:
		raise EzCLIError('the language [{language}] isn\'t supported')

	CONFIG.done()
