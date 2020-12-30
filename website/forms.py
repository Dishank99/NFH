from django.forms import ModelForm
import django.forms as forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
    label=("Password *"),
    strip=False,
    widget=forms.PasswordInput,
    # help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=("Confirm Password *"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
        ]
        help_texts = {
            'username': None,
            'email': None,
        }

