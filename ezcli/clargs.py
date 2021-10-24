import sys as _sys
from re import compile as _re

from . import _config
from . import _prebuilt
from ._error import EzCLIError as _exc

__all__ = ['arguments', 'config', 'OPTFLAG']

_shortopt = _re(r'(-)([a-z])(=.*)')
_concatopts = _re(r'(-)([a-z]+)')
_longopt = _re(r'(--)([a-z\-])(=.*)')

_short = _re(r'^-[a-z]$')
_long = _re(r'^--[a-z\-]+$')

class OptionType:
	def __init__(self, t):
		self._type_name = t

	def __repr__(self):
		return f'<option type {self._type_name}>'
	
OPTFLAG = OptionType('FLAG')

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

_opts = list()
_args = list()

def arguments(*args):
	_parse_args()

	values = [_checkfor(arg) for arg in args]
	if _checkfor(('-h', '--help', OPTFLAG)):
		_print_help_msg()
	if len(values) == 1:
		return values[0]
	else:
		return tuple(values)

def _parse_args():
	parsing_options = True
	for arg in _sys.argv[1:]:
		if parsing_options:
			if m := _shortopt.fullmatch(arg):
				g = m.groups()
				if g[2]:
					_args.append((g[1], _cutq(g[2])))
				else:
					_args.append((g[1], None))
			elif m := _concatopts.fullmatch(arg):
				g = m.groups()
				for a in g[1]:
					_args.append((a, None))
			elif m := _longopt.fullmatch(arg):
				g = m.groups()
				if g[2]:
					_args.append((g[1], _cutq(g[2])))
				else:
					_args.append((g[1], None))
			else:
				parsing_options = False
		if not parsing_options:
			_args.append((None, _cutq(arg)))
	print(_args)

def _cutq(val):
	if val.startswith('="'):
		val = val[2:]
	else:
		val = val[1:]
	if val.endswith('"'):
		return val[:i-1]
	else:
		return val

def _checkfor(arg):
	if isinstance(arg, tuple):
		short = list()
		long = list()
		type = OPTFLAG
		scan = 0
		for spec in arg:
			if scan == 0:
				if isinstance(spec, str):
					if _short.match(spec):
						short.append(spec[1:])
					else:
						scan = 1
				else:
					scan = 1
					
			if scan == 1:
				if isinstance(spec, str):
					if _long.match(spec):
						long.append(spec[2:])
					else:
						scan = 2
				else:
					scan = 2
					
			if scan == 2:
				if isinstance(spec, OptionType):
					type = spec
				elif isinstance(spec, str):
					desc = spec
					scan = 3
				else:
					raise EzCLIError(f'Expected the option type or description, got {spec} instead')
					
			if scan == 3:
				raise EzCLIError(f'Got unexpected {spec} in an option')
					
		if not (short or long):
			raise EzCLIError('An option must have at least one form')
			
	else:
		raise EzCLIError("Options should be given as tuples like ('-a', '--myoption'). See the documentation for more details")
			
			
		
		