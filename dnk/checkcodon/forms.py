from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CodonFindForm(forms.Form):
    codon = forms.CharField(label='Ваша последовательность', max_length=3, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_codon(self, *args, **kwargs):
        codon = self.cleaned_data['codon']
        for c in codon:
            if not c.lower() in ['a', 'c', 'g', 't']:
                raise forms.ValidationError('Кодон может содержать только буквы A, C, G, T')
        return self.cleaned_data['codon']


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Подтверждение пароля",
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
