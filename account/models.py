import stripe

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


class Membership(models.Model):
    TYPES = (
        ('Free', 'free',),
        ('Yearly', 'yearly',),
        ('Lifetime', 'lifetime',),
    )
    slug = models.SlugField(max_length=255)
    member_type = models.CharField(choices=TYPES, max_length=10)
    price = models.FloatField()
    stripe_plan_id = models.CharField(max_length=255)

    def __str__(self):
        return f'Membership {self.member_type}'

class UserMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=40)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'UserMembership {self.user.username}'

class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership, on_delete = models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=40)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Subscription {self.user_membership.user.username}'


# Creating signalsdasdfadfadfasdsd
# @receiver(post_save, sender=User)
# def post_save_create_membership(sender, instance, created, **kwargs):
#     if created:
#         UserMembership.objects.get_or_create(user=instance)

#     user_membership, created = UserMembership.objects.get_or_create(user=instance)

#     if user_membership.stripe_customer_id == None or user_membership.stripe_customer_id == '':
#         new_customer_id = stripe.Customer.create(email=instance.email)
#         user_membership.stripe_customer_id = new_customer_id['id']
#         user_membership.save()