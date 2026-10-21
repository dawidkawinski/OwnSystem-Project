from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Twoje imię'
        self.fields['surname'].widget.attrs['placeholder'] = 'Twoje nazwisko'
        self.fields['email'].widget.attrs['placeholder'] = 'Adres e-mail'
        self.fields['password1'].widget.attrs['placeholder'] = 'Hasło'
        self.fields['password2'].widget.attrs['placeholder'] = 'Powtórz hasło'
        for field in self.fields.values():
            field.label = ''