import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meuprojeto.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = 'cassio'
email = 'cadanm97@gmail.com'
password = 'admin@1397'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print('Superuser criado com sucesso.')
else:
    print('Superuser já existe.')
