# from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User, PermissionsMixin

# for token generation
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



class MyUserManager(BaseUserManager):
    # def create_user(self, email, date_of_birth, password=None):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        # user = self.model(
        #     email=self.normalize_email(email),
        #     date_of_birth=date_of_birth,
        # )
        user = self.model(
            email=self.normalize_email(email),
            is_admin=True
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_superuser(self, email, date_of_birth, password=None):
    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        # user = self.create_user(
        #     email,
        #     password=password,
        #     date_of_birth=date_of_birth,
        # )
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=100, editable=True, null=True)
    # date_of_birth = models.DateField()
    # mobile_number = models.CharField(max_length=15, editable=True, unique=True, null=True)
    # last_login_time = models.DateTimeField(null=True, blank=True)
    # last_logout_time = models.DateTimeField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # def get_short_name(self):
    #     "Returns the short name for the user."
    #     return self.first_name
    #
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
