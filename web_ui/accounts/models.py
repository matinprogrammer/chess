from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator
from .managers import UserManager
from django.db import models


class User(AbstractBaseUser):
    phone_number = models.CharField(
        unique=True, validators=[RegexValidator(r'^09[0-3,9][0-9]{8}$')]
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    joined_data = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["first_name"]

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, perm, obj=None):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return str(self.phone_number)
