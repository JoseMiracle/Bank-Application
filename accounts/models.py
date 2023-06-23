# Create your models here.
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, AbstractUser
from banks.models import Banks
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class Client(AbstractUser):
    ACCOUNT_TYPE = (
        ("savings", "savings"),
        ("current", "current"),
        ("student", "student"),
    )
    username = None
    bank = models.ForeignKey(Banks, on_delete=models.CASCADE)
    email = models.EmailField(_("email address"), blank=False, null=False, unique=True)
    other_name = models.CharField(max_length=70, blank=True)
    image = models.ImageField(upload_to="images/")
    account_number = models.CharField(max_length=10)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE)
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    home_address = models.CharField(max_length=250)
    account_balance = models.IntegerField(default=0)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
