from django.contrib.auth.forms import UserCreationForm
from work.models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'password1',
            'password2',
            'email',
            'username',
        ]
