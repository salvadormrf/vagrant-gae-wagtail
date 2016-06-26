#!/usr/bin/env python
import os
import sys


def add_extra_paths():
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'vendor'))


if __name__ == "__main__":
    add_extra_paths()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
