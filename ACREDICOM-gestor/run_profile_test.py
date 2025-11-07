import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestor.settings')
django.setup()

from accounts.models import Profile

# Tu código aquí
print(Profile.objects.all())
