from django.contrib.auth.forms import PasswordResetForm
from django.core.exceptions import ValidationError
from main.models import AdvUser

class EmailValidationOnForgotPassword(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if not AdvUser.objects.filter(email__iexact=email, is_active=True).exists():
            raise ValidationError("Пользователь с указанным адресом электронной почты не зарегистрирован!")
        return email

