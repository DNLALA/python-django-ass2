from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    PERSON_TYPE = (
        (1, 'Patient'),
        (2, 'Doctor'),
    )
    Person = forms.ChoiceField(
        choices=PERSON_TYPE,
        widget=forms.RadioSelect()
    )
    email = forms.EmailField()
    First_Name = forms.CharField()
    Last_Name = forms.CharField()

    class Meta:
        model = User
        fields = ['Person', 'First_Name', 'Last_Name',
                  'username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    First_Name = forms.CharField()
    Last_Name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
