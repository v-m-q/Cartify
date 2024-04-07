"""
WSGI config for main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

application = get_wsgi_application()

class Inspect:
    @staticmethod
    def monkeypatch():
        import inspect
        print('Applying monkeypatch for inspect')
        if hasattr(inspect, 'getfullargspec') and not hasattr(inspect, 'getargspec'):
            def getargspec(func):
                from collections import namedtuple
                inspect_result = inspect.getfullargspec(func)
                ArgSpec = namedtuple('ArgSpec', 'args varargs keywords defaults')
                return ArgSpec(
                    inspect_result.args, inspect_result.varargs,
                    inspect_result.varkw, inspect_result.defaults
                )
            inspect.getargspec = getargspec

Inspect.monkeypatch()
# app = application