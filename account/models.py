from django.forms import ValidationError
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone




class UserManager(BaseUserManager):
    def create_user(self, email, username=None, password=None, is_active=True, is_staff=False,
                    is_admin=False):
        if not email:
            raise ValueError("User must provide an email")
        if not password:
            raise ValueError("User must provide a password")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.active = is_active
        user.admin = is_admin
        user.staff = is_staff
        user.save(using=self._db)
        return user

    def create_staff(self, email, username=None, password=None):
        user = self.create_user(email=email, username=username, password=password, is_staff=True)
        return user

    def create_superuser(self, email, username=None, password=None):
        user = self.create_user(email=email, username=username, password=password, is_staff=True, is_admin=True)
        return user

    def get_staffs(self):
        return self.filter(staff=True)

    def get_admins(self):
        return self.filter(admin=True)


class User(AbstractBaseUser):
    username = models.CharField(max_length=225, null=True)
    email = models.EmailField(max_length=255, unique=True)

    # Admin fields
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now=True)
    
    # Field for disabled accounts
    disabled = models.BooleanField(default=False)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return f'User {self.email}'

    # def get_absolute_url(self):
    #     return reverse('profile', kwargs = [self.id])

    def email_user(self, subject, message, fail=True):
        print(message)
        val = send_mail(subject=subject, message=message, from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=[self.email], fail_silently=fail)
        return True if val else False

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    class Meta:
        verbose_name = 'LightLab User'