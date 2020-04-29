from .models import Profile
from django import forms
from django.contrib.auth.models import User

import string


class UserRegistrationForm(forms.ModelForm):
    """Form for user registration"""

    password = forms.CharField(label='Введіть пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторіть пароль', widget=forms.PasswordInput)


    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ця електронна пошта вже використовується!")

        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Цей логін вже використовується')

        return self.cleaned_data


    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email')
        help_texts = {
            'username': "Обов'язкове поле. Не більше 150 символів.",
        }


    def clean_password2(self):
        cleanedData = self.cleaned_data
        #TODO: make it django way 
        password = cleanedData['password']
        has_no = set(password).isdisjoint
        if len(password) < 8:
            raise forms.ValidationError('Мінімальна довжина пароля - 8 символів.')
        elif has_no(string.digits):
            raise forms.ValidationError('Пароль має містити хоча б одну цифру.')
        elif has_no(string.ascii_lowercase):
            raise forms.ValidationError('Пароль має містити хоча б один символ у нижньому регістрі.')
        elif has_no(string.ascii_uppercase):
            raise forms.ValidationError('Пароль має містити хоча б один символ у верхньому регістрі.')
        
        
        if cleanedData['password'] != cleanedData['password2']:
            raise forms.ValidationError('Паролі не співпадають')
        return cleanedData['password2']


class ProfileRegistrationForm(forms.ModelForm):
    """form for user profile registration"""

    birthdate = forms.DateField(label='Дата народження', input_formats=['%m/%d/%Y'], required=False)
    
    class Meta:
        model = Profile
        fields = ('isLecturer', 'birthdate', 'group', 'faculty', 'cathedra')


class UserEditForm(forms.ModelForm):
    """Form for edit user info"""


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def clean(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ця електронна пошта вже використовується!")
       return self.cleaned_data


class ProfileEditForm(forms.ModelForm):
    """Form to edit user profile info"""
    
    # TODO: Fix is_valid() when solo send choicefields returns False, but with another fields return True

    birthdate = forms.DateField(label='Дата народження', input_formats=['%m/%d/%Y'], required=False)

    class Meta:
        model = Profile
        fields = ('birthdate', 'group', 'faculty', 'cathedra')