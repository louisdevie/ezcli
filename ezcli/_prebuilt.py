'''pre-built text'''

AVAILABLE_LANGUAGES = [
	'en', 'fr',
]

INCOMPLETE_LANGUAGES = [
	
]

TEXT = {
	# default application name
	'NO_NAME':      {'en': '[application name]',	   'fr': '[nom de l\'application]'},

	# default application version
	'NO_VERSION':   {'en': '[unknown]',                'fr': '[inconnue]'},

	# application introduction
	'APP_IDENTITY': {'en': '{name} version {version}', 'fr': '{name} version {version}'},

	# ...
	'CMD_USAGE':    {'en': 'Usage :',                  'fr': 'Utilisation :'},
}

from .conf import CONFIG

def __getattr__(attr):
	if attr == 'available':
		return AVAILABLE_LANGUAGES
	elif attr == 'incomplete':
		return INCOMPLETE_LANGUAGES
	else:
		return TEXT[attr].get(CONFIG.LANGUAGE, TEXT[attr]['en'])