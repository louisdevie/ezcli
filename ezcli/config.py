class config:
	NAME = str()
	VER = str()
	LANG = str()
	
CONF = config()
	
def config(appname='%?', appversion='%?', language='en'):
	if _config.DONE:
		raise _exc('ezCLI is already configured')

	_config.DONE = True
	if appname == '%?':
		_config.NAME = _prebuilt.noname()
	else:
		_config.NAME = appname

	if appversion == '%?':
		_config.VER = _prebuilt.noversion()
	else:
		_config.VER = appversion

	if language in _prebuilt.AVAILABLE_LANGUAGES:
		_config.LANG = language
		if language in _prebuilt.INCOMPLETE:
			raise _wrn('the language "{language}" isn\'t fully supported') 
	else:
		raise _exc('the language "{language}" isn\'t supported')
