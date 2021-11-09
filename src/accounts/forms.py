from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password

User = get_user_model()

class UserLoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': ('form', 'input-form', 'h1', 'a')}),
                            label=' Введите e--mail',
                            )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': ('form', 'input-form', 'h1', 'a')}),
                               label=' Введите пароль',
                               )

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email') #.strip()         # cleaned_data.get('email') - выбираем из всех данных (которые поступают с методом POST email и password в чистом виде
        password = self.cleaned_data.get('password') #.strip()   #.strip() - убирает пробел в конце если его нечайно добавил пользователь

        if email and password:
            qs = User.objects.filter(email=email)
            if not qs.exists():
                raise forms.ValidationError('Такого пользователя нет!')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Пароль не верный!')
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('Данный аккаунт отключен!')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': ('form', 'input-form', 'h1', 'a')}),
                            label='Введите Ваш e--mail  ',
                            )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': ('form', 'input-form', 'h1', 'a')}),
                               label='Введите Ваш пароль  ',
                               )
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': ('form', 'input-form', 'h1', 'a')}),
                               label='Введите пароль снова',
                               )

    class Meta:
        model = User
        fields =('email',)

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return data['password2']