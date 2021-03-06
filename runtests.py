#!/usr/bin/env python
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

from django.test.utils import get_runner  # noqa isort:skip
from django.conf import settings  # noqa isort:skip
from django.core.management import execute_from_command_line # noqa isort:skip
import django  # noqa isort:skip

if django.VERSION >= (1, 7):
    django.setup()


def runtests():
    execute_from_command_line([sys.argv[0], "test"])
    #TestRunner = get_runner(settings)
    #test_runner = TestRunner(verbosity=1, interactive=True)
    #failures = test_runner.run_tests(['tests'])
    #sys.exit(bool(failures))


if __name__ == '__main__':
    runtests()
