import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django

django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = 'admin'
email = 'admin@example.com'
password = 'Admin@123'

if User.objects.filter(username=username).exists():
    print(f'superuser already exists: {username}')
else:
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'created superuser: {username}')
