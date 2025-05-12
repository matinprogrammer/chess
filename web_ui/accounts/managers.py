from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password, first_name, **extra_fields):
        if not phone_number:
            raise ValueError("Users must have phone number")

        if not first_name:
            raise ValueError("Users must have fist name")

        if not password:
            raise ValueError("Users must have password")

        user = self.model(
            phone_number=phone_number,
            first_name=first_name,
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, first_name, **extra_fields):
        user = self.create_user(
            phone_number=phone_number,
            first_name=first_name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
