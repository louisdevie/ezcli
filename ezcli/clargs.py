import sys as _sys

from . import _prebuilt
from .conf import CONFIG
from ._error import EzCLIError
from . import _utils

__all__ = ['arguments']

REGEX_SHORT_OPTION = _utils.regex(r'(-)([a-z])(=.*)?')
REGEX_MULTIPLE_OPTIONS = _utils.regex(r'(-)([a-z]+)')
REGEX_LONG_OPTION = _utils.regex(r'(--)([a-z\-]+)(=.*)?')

REGEX_SHORT_TEMPLATE = _utils.regex(r'^-[a-z]$')
REGEX_LONG_TEMPLATE = _utils.regex(r'^--[a-z\-]+$')


class Parameter: pass
class Option: pass


def arguments(*params):
	args = parse_args()

	values = [_checkfor(p) for p in params]

	if _checkfor(('-h', '--help', OPTFLAG)):
		_print_help_msg()
		exit(0)

	if len(values) == 0:
		return None

	elif len(values) == 1:
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
			
			
		
		