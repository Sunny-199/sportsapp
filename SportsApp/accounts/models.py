from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin, )


GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),)

ROLE = (('user', 'User'),
        ('coach', 'Coach'),
        ('owner', 'Owner'))


SPECIALISATION_CHOICES =(
    ('cardio', 'cardio'),
    ('strength', 'strength')
)


class UserManager(BaseUserManager):
    def _create_user(self, email: str, password: str = None, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, email: str = None, password=None, **kwargs):
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email=email, password=password, **kwargs)


    def create_superuser(self, email, password, **kwargs):

        kwargs.setdefault('is_superuser', True)
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self._create_user(email=email, password=password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        'email address',
        max_length=255,
        unique=True,
        error_messages={'unique': "A user with that email already exists.", }
    )
    name = models.CharField(max_length=100, unique=False)
    is_active = models.BooleanField('active',
                                    default=True,
                                    help_text=('Designates whether this user should be treated as active. '
                                               'Unselect this instead of deleting accounts.'
                                               ),
                                    )
    is_staff = models.BooleanField('staff status',
                                   default=False,
                                   help_text='Designates whether the user can log into this admin site.',
                                   )
    role = models.CharField(max_length=20, choices=ROLE, default='owner')
    # USERNAME_FIELD = 'email'
    username = None
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:

        db_table = "custom_user"
        verbose_name = 'user'
        verbose_name_plural = 'users'

class VerifyOtp(models.Model):


    email = models.EmailField()
    query_string = models.CharField(max_length=50)
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.query_string

    class Meta:
        db_table = "verify_otp"

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user_profile')
    phone_no = models.CharField(max_length=255, null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    sports_center_name = models.CharField(max_length=255, null=True, blank=True)
    from_time = models.TimeField(null=True, blank=True)
    to_time = models.TimeField(null=True, blank=True)
    specialisation = models.CharField(max_length=255, choices=SPECIALISATION_CHOICES, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, null=True, blank=True)
    status = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = "user_profile"


