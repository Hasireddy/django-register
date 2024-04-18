from django import forms
from signupForm.models import Register
from django.core import validators


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
