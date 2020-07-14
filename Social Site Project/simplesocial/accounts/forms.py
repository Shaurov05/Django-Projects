from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __int_it(self, **kwargs):
        super().__int__(*args,**kwargs)
        self.fields['username'].lebel = 'Display Name'
        self.fields['email'].label = "Email Address"
