from django import forms
from .models import Register
from .models import Login
from .models import WasteDetails
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import SetPasswordForm
import datetime


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
            "username": {"unique": ("A user with that username already exists.")},
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
        cleaned_data = super().clean()
        first_name = cleaned_data["first_name"]
        if not first_name.isalpha():
            #   raise forms.ValidationError('Please enter a real name.')
            message = "First name must contain only characters"
            self.add_error("first_name", message)
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update()
        # Iterate over each form field and add the 'form-control' class
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        # fields = "_all_",
        fields = ["username", "password"]


class WastedataForm(forms.ModelForm):
    class Meta:
        model = WasteDetails
        fields = [
            "year",
            "waste_type",
            "disposer",
            "value",
            "recycling_method",
            "recycle_description",
        ]

        # widgets = {
        #     "year": forms.(
        #         attrs={"placeholder": "Enter your First name"},
        #     ),}
        #     "waste_type": forms.TextInput(
        #         attrs={"placeholder": "Enter your Last name"}
        #     ),
        #     "disposer": forms.TextInput(attrs={"placeholder": "Enter your Username"}),
        #     "value": forms.TextInput(attrs={"placeholder": "Enter your Username"}),
        # "recycling_method": forms.ChoiceField(
        #     choices=RECYCLING_CHOICES,
        #     attrs={
        #         "id": "RoomTypeDropDownList",
        #         "class": "form-control form-control-lg  select",
        #     },
        # ),
        #     "recycle_description": forms.TextInput(
        #         attrs={"placeholder": "Enter your Username"}
        #     ),
        # }
        labels = {
            "year": "year",
            "waste_type": "waste_type",
            "disposer": "disposer",
            "value": "value",
            "recycling_method": "recycling_method",
            "recycle_description": "recycle_description",
        }
        error_css_class = "error-field"
        error_messages = {
            "value": {
                "required": "The first name should not be empty",
                "max_length": "maximum length allowed is 20",
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["waste_type"].widget.attrs.update()
        self.initial["recycling_method"] = WasteDetails._meta.get_field(
            "recycling_method"
        ).get_default()
        # Iterate over each form field and add the 'form-control' class
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
        self.fields["year"].widget.attrs.update({"class": "form-select"})
