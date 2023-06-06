from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"placeholder": "Username"}),
    )
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
    )


class SignupForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"placeholder": "Username"}),
    )
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
    )
    password_confirmation = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
    )
