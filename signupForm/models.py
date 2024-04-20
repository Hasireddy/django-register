from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError

# Create your models here.

validators.DecimalValidator


class PrefixValidator:
    def __init__(self, prefix: str = None):
        # `self` keyword stores the reference of the object which has called method.
        self.prefix = prefix

    def __call__(self, value: str):
        if not self.prefix is None and not value.startswith(self.prefix):
            raise ValidationError(f"The value must start with {self.prefix}")


# Types of Methods in Class:
# 1. Instance Method
# 2. Class Method


class Register(models.Model):
    first_name = models.CharField(max_length=20, validators=[PrefixValidator("A")])
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField(
        validators=[validators.EmailValidator(message="Invalid Email")],
    )
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)


class Login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
