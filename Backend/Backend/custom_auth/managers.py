from django.contrib.auth.models import UserManager
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from Backend.custom_auth.validators import validate_over_LIMIT_AGE


class CustomManager(UserManager):
    def _create_user(self, email, date_of_birth, password=None, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        if not email:
            raise ValueError("The given email must be set.")
        try:
            validate_over_LIMIT_AGE(date_of_birth)
        except ValidationError:
            raise ValueError("The user is not over 16 years of age.")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        user = self.model(email=email, date_of_birth=date_of_birth)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self._create_user(email, date_of_birth, password, **extra_fields)

    def create_user(self, email, date_of_birth, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, date_of_birth, password, **extra_fields)



