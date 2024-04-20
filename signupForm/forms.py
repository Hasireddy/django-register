from django import forms
from .models import Register
from .models import Login
from django.core import validators
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        # fields = "_all_",
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]
        labels = {
            "first_name": "First name",
            "last_name": "Last name",
            "user_name": "Username",
            "email": "Email",
            "password1": "Password",
            "password2": "Confirm Password",
        }
        widgets = {
            "first_name": forms.TextInput(
                attrs={"placeholder": "Enter your First name"},
            ),
            "last_name": forms.TextInput(attrs={"placeholder": "Enter your Last name"}),
            "username": forms.TextInput(attrs={"placeholder": "Enter your Username"}),
            "email": forms.EmailInput(attrs={"placeholder": "Enter your Email"}),
            "password1": forms.PasswordInput(
                attrs={"placeholder": "Enter your Password"}
            ),
            "password2": forms.PasswordInput(
                attrs={"placeholder": "Confirm your Password"}
            ),
        }

        error_css_class = "error-field"
        error_messages = {
            "first_name": {
                "required": "The first name should not be empty",
                "max_length": "maximum length allowed is 20",
            },
            "last_name": {
                "required": "The Last name should not be empty",
                "max_length": "maximum length allowed is 20",
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data["password1"]
        password2 = cleaned_data["password2"]
        if not password2:
            message = "You must confirm your password"
            self.add_error("password2", message)
            # raise forms.ValidationError("You must confirm your password") Non field errors
        if password1 != password2:
            message = "Your passwords do not match"
            self.add_error("password2", message)
            # raise forms.ValidationError("Your passwords do not match")
            return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for displaying placeholder
        # for field in self.fields:
        #     print(field)
        #     self.fields[str(field)].widget.attrs.update(
        #         placeholder=f"Enter your {str(field)}",
        #     )
        self.fields["first_name"].widget.attrs.update()
        # Iterate over each form field and add the 'form-control' class
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        # fields = "_all_",
        fields = ["username", "password"]
