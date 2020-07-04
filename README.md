1、新式类
2、面向对象
3、设计模式



django源码跟踪


python manage.py  runserver 8080

from django.core.management import execute_from_command_line

execute_from_command_line((runserver,8080))

venv/lib/python3.7/site-packages/django/core/management/__init__.py

def execute_from_command_line(argv=None):
    """Run a ManagementUtility."""
    utility = ManagementUtility((runserver,8080))
    utility.execute()

from collections import OrderedDict, defaultdict
from django.conf import settings
from django.core.management.base import (
    BaseCommand, CommandError, CommandParser, handle_default_options,
)

class ManagementUtility:
    """
    Encapsulate the logic of the django-admin and manage.py utilities.
    """
    def __init__(self, argv=(runserver,8080)):
        self.argv = argv or sys.argv[:]
    
    def execute(self):
        subcommand = runserver
        self.fetch_command(runserver).run_from_argv(8080)

    def fetch_command(self, subcommand):

            klass = load_command_class(runserver, subcommand)

def load_command_class(app_name, name):

    module = import_module('%s.management.commands.%s' % (app_name, name))
    return module.Command()

runserver.py.Command().run_from_argv(8080)

django/contrib/staticfiles/management/commands/runserver.py run_from_argv(8080)
django/core/management/commands/runserver.py
django/core/management/base.py

self.execute(*args, **cmd_options)

def get_handler(self, *args, **options):

def get_internal_wsgi_application():
    return WSGIHandler()