from pathlib import Path

base = Path(__file__).resolve().parent
users_init_source = base / 'users' / '__init.py__'
users_init_target = base / 'users' / '__init__.py'
if users_init_source.exists():
    users_init_source.rename(users_init_target)

manage_py = base / 'manage.py'
manage_py.write_text(
"""#!/usr/bin/env python
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            'Could not import Django. Are you sure it is installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?'
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
""",
encoding='utf-8'
)
print('repair_manage.py run successfully')
