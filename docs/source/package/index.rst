Package documentation
=====================

Functions
---------

.. py:function:: ezcli.config([appname,] [appversion,] [language='en'])
   
   Configure ezCLI.

   :param str appname: The name of the application
   :param str appversion: The version of the application
   :param str language: The language to use for auto-generated content
   :rtype: None
   :raises EzCLIError: if ezCLI is already configured, or if the language isn't supported

.. py:function:: ezcli.arguments(opt1, opt2, ..., param1, param2, ...)
   
   Parse command-line arguments. If a ``-h`` or ``--help`` argument is given, display an auto-generated help message and exits.

   :param tuple opt1,opt2,...: the command-line options of the application. they're tuples like ``('-a', '--my-option', TYPE, 'description')`` where ``'-a'`` and ``'--my-option'`` are the forms the option can take (at least one), ``TYPE`` is the option type and ``'description'`` its description.
   :param ParameterType param1,param2,...: the command-line parameters of the application. they shold always be given *after* the options.
   :returns: None if the app takes no arguments, the value of the option/parameter if there's only one, else a tuple with the value of each of the options, in the order they were passed to the function.
   :raises EzCLIError: If an option isn't valid or given after a parameter