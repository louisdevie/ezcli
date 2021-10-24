'''pre-built text/content in different languages'''

AVAILABLE_LANGUAGES = [
	'en',
	'fr',
]

INCOMPLETE = []

NO_NAME = { # default application name
	'en': '[application name]',
	'fr': '[nom de l\'application]'
}

NO_VERSION = { # default application version
	'en': '[unknown]',
	'fr': '[inconnue]'
}

from . import _config

def _get(table, lang):
	return table.get(lang, table.get('en', ''))

def noname():
	return _get(NO_NAME, _config.LANG)

def noversion():
	return _get(NO_VERSION, _config.LANG)