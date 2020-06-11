from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Ho',
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Ho',
    )
    email = forms.EmailField(
        max_length=100,
        required=True,
        help_text='Valid email required',
    )
    date_of_birth = forms.DateField()

    class Meta:
        model = User
        fields  = [
            'first_name',
            'last_name',
            'username',
            'email',
            'date_of_birth',
            'gender',
            'password1',
            'password2',
        ]