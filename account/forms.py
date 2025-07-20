from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password2 is None or password1 is None or password1!=password2:
            raise forms.ValidationError('Passwords don\'t match')
        return password2


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=120, label='Login')
    password = forms.CharField(label='Parol', widget=forms.PasswordInput)


class PassChangeForm(forms.Form):
    old_pass = forms.CharField(label='Old password', widget=forms.PasswordInput)
    new_pass = forms.CharField(label='New password', widget=forms.PasswordInput)
    confirm_pass = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    code = forms.CharField(label='Code sent to email', max_length=6)


    def clean(self):
        clean_data = super().clean()
        new_pass = self.cleaned_data['new_pass']
        confirm_pass = self.cleaned_data['confirm_pass']
        if new_pass != confirm_pass:
            raise forms.ValidationError('Passwords don\'t match')
        return clean_data


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets= {'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-xl'
            })}

