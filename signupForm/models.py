from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.validators import UnicodeUsernameValidator

# Create your models here.


class PrefixValidator:
    def __init__(self, prefix: str = None):
        # `self` keyword stores the reference of the object which has called method.
        self.prefix = prefix

    def __call__(self, value: str):
        if not self.prefix is None and not value.startswith(self.prefix):
            raise ValidationError(f"The value must start with {self.prefix}")


# class AlphaValidator:
#     def __init__(self, message=None):
#         self.message = message or "Only alphabetic characters are allowed."

#     def __call__(self, value):
#         if not str(value).isalpha():
#             raise ValidationError(self.message)


# Types of Methods in Class:
# 1. Instance Method
# 2. Class Method


class Register(models.Model):
    # first_name = models.CharField(max_length=20, validators=[PrefixValidator("A")])
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        max_length=20, validators=[username_validator], unique=True
    )
    email = models.EmailField(
        unique=True,
        validators=[validators.EmailValidator(message="Invalid Email")],
    )
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)


class Login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
