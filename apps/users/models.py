from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import BaseModel
from apps.users.choices import Role


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError("The given phone number must be set")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(phone_number, password, **extra_fields)


class User(AbstractUser, BaseModel):
    phone_number = PhoneNumberField(
        verbose_name=_("Phone number"),
        max_length=16,
        unique=True,
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)

    username = models.CharField(verbose_name=_("username"), max_length=150, unique=True, blank=True, null=True)
    email = models.EmailField(verbose_name=_("Email"), null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "phone_number"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return str(self.phone_number)

    def save(self, *args, **kwargs):
        if self.phone_number:
            user = User.objects.filter(phone_number=self.phone_number).first()
            if user and user.id != self.id:
                raise ValidationError(_("User with this phone number already exists."))
        super().save(*args, **kwargs)


class Profile(BaseModel):
    user = models.ForeignKey(User, related_name="profile", verbose_name=_("User"), on_delete=models.CASCADE)
    image = models.ImageField(verbose_name=_("Profile Image"), unique="user_image/")
    info = models.TextField(verbose_name=_("Info"), null=True, blank=True)
    role = models.CharField(_("Role"), max_length=55, choices=Role.choices, default=Role.simple_user)
    telegram = models.URLField(verbose_name=_("Telegram"), null=True, blank=True)
    instagram = models.URLField(verbose_name=_("Instagram"), null=True, blank=True)
    facebook = models.URLField(verbose_name=_("Facebook"), null=True, blank=True)
    twitter = models.URLField(verbose_name=_("Twitter"), null=True, blank=True)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.surname
