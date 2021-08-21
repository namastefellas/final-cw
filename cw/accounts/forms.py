from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django import forms
from accounts.models import Profile




class MyUserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Password", strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Confirm password", required=True, widget=forms.PasswordInput, strip=False)
    email = forms.CharField(label='Email', required=True)
    phone_number = forms.CharField(label='Phone Number', required=True)

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords don't match!")
        if not first_name and not last_name:
            raise forms.ValidationError("Please, fill one of the fields")


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            Profile.objects.create(user=user)
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ('user',)

class UserUpdateFrom(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')
