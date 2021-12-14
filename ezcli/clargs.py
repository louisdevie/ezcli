from . import _prebuilt, _utils
from .conf import CONFIG
from ._error import EzCLIError

__all__ = ['arguments']

REGEX_SHORT_OPTION = _utils.regex(r'(-)([a-z])(=.*)?')
REGEX_MULTIPLE_OPTIONS = _utils.regex(r'(-)([a-z]+)')
REGEX_LONG_OPTION = _utils.regex(r'(--)([a-z\-]+)(=.*)?')

REGEX_SHORT_FORM = _utils.regex(r'-[a-zA-Z]')
REGEX_LONG_FORM = _utils.regex(r'--[a-zA-Z\-]+')


class Parameter: pass

class BaseOption:
	def __init__(self, *forms, unique=False, description=None):
		self.short_forms = list()
		self.long_forms = list()
		self.isunique = unique
		self.description = description

		for form in forms:
			if REGEX_SHORT_FORM.fullmatch(form):
				self.short_forms.append(form[1:])

			elif REGEX_LONG_FORM.fullmatch(form):
				self.long_forms.append(form[2:])

			else:
				raise EzCLIError('Option forms must be given as "-a" or "--abc" and can only contain letters and hyphens')

	def __repr__(self):
		return type(self).__name__ + '(' + ', '.join(
			['-'+f for f in self.short_forms] + 
			['--'+f for f in self.long_forms]) + ')'

	def __str__(self):
		return repr(self)

	def lookup(self, arguments):
		eaten = list()
		found = list()

		for i, arg in enumerate(arguments):
			opt, val = arg
			if opt in self.short_forms+self.long_forms:
				found.append(val)
				eaten.insert(0, i)
				if self.isunique: break

		for i in eaten:
			del arguments[i]

		return found


class FlagOption (BaseOption):
	def __init__(self, *forms):
		super().__init__(*forms, unique=True)

	def lookup(self, arguments):
		return bool(super().lookup(arguments))


def arguments(*params):
	args = parse_args()

	values = [p.lookup(args) for p in params]

	help_option = FlagOption('-h', '--help')
	print(help_option)

	if help_option.lookup(args):
		print_help_msg(args)
		exit(0)

	if len(values) == 0:
		return None

	elif len(values) == 1:
		return values[0]

	else:
		return tuple(values)

def parse_args():
	args_found = list()

	parsing_options = True
	for arg in _utils.argv:
		if parsing_options:
			if m := REGEX_SHORT_OPTION.fullmatch(arg):
				g = m.groups()
				if g[2]:
					args_found.append((g[1], _utils.strip(g[2])))
				else:
					args_found.append((g[1], None))

			elif m := REGEX_MULTIPLE_OPTIONS.fullmatch(arg):
				g = m.groups()
				for a in g[1]:
					args_found.append((a, None))

			elif m := REGEX_LONG_OPTION.fullmatch(arg):
				g = m.groups()
				if g[2]:
					args_found.append((g[1], _utils.strip(g[2])))
				else:
					args_found.append((g[1], None))

			else:
				parsing_options = False
				args_found.append((None, _utils.strip(arg)))

		else:
			args_found.append((None, _utils.strip(arg)))

	print(args_found)
	return args_found