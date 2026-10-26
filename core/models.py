from django.contrib.auth.models import AbstractUser
from django.db import models
import secrets

class User(AbstractUser):
    is_lecturer = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_candidate = models.BooleanField(default=False)

def generate_id():
    while True:
        kandydat = ''.join(secrets.choice('0123456789') for _ in range(6))
        if not User.objects.filter(username=kandydat).exists():
            return kandydat

