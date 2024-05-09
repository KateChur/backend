from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.contrib.auth.hashers import make_password


class RegistrationForm(forms.ModelForm):
    # password_check = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

    # def clean(self):
    #     password_1=self.cleaned_data['password']
    #     password_2=self.cleaned_data['password_check']
    #
    #     if password_1 != password_2:
    #         raise ValidationError("Passwords do not match!")
    #     return self.cleaned_data

    # def save(self):
    #     # self.cleaned_data.pop('password_check')
    #     User.set_password(self.cleaned_data["password"])
    #     return User.objects.create_user(**self.cleaned_data)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.password = make_password(self.cleaned_data['password'])
        # hasher = PBKDF2PasswordHasher()
        # user.password = hasher.encode(sha1_hash, salt)
        if commit:
            user.save()
        return User.objects.create_user(**self.cleaned_data)
