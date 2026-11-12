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


class Ocena(models.Model):
    student = models.ForeignKey(
        User,
        to_field='username',
        db_column='student_id',
        on_delete=models.CASCADE,
        related_name='oceny',
        limit_choices_to={'is_student': True},
    )
    przedmiot = models.CharField(max_length=100)
    wartosc = models.DecimalField(max_digits=2, decimal_places=1)
    data_wystawienia = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.username}: {self.przedmiot} ({self.wartosc})'