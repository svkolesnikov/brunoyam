from django import forms
from .models import AdvUser

from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from .signals import post_register


class ProfileEditForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='E-mail')

    class Meta:
        model = AdvUser
        fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'sex', 'birthday')


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='E-mail')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Пароль повторно', widget=forms.PasswordInput, help_text='Введите пароль еще раз')

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()

        #password1 = self.cleaned_data['password1']
        password1 = self.cleaned_data.get('password1', None)
        print(f'password1 = {password1}')

        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError('Введенные пароли не совпадают')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        user.is_activated = True
        if commit:
            user.save()
        post_register.send(RegisterForm, instance=user)
        return user

    class Meta:
        model = AdvUser
        fields = ('username', 'password1', 'password2', 'email',  'first_name', 'last_name', 'phone', 'address', 'sex', 'birthday')

