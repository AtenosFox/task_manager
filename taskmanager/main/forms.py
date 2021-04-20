from .models import Task
from django.forms import ModelForm, TextInput, Textarea
from django import forms
from django.contrib.auth.models import User


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название задачи',
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание задачи'
            })
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        password = forms.CharField(widget=forms.PasswordInput)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].label = 'Логин'
            self.fields['password'].label = 'Пароль'

        def clean(self):
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not User.objects.filter(username=username).exists():
                raise forms.ValidationError(f'Пользователь с логином {username} не зарегистрирован в системе')
            user = User.objects.filter(username=username).first()
            if user:
                if not user.check_password(password):
                    raise forms.ValidationError("Неверный пароль")
            return self.cleaned_data
