from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.


class UserProfileManager(BaseUserManager):
    # A Docstring
    """Helps Django work with our custom User Profile model."""

    def create_user(self, email, name, password=None):
        """Creates a new User Profile object."""

        if not email:
            raise ValueError('User must have an e-mail address.')

        email = self.normalize_email(email)
        # Here we actually create a new object
        user = self.model(email=email, name=name)
        # This function will encrypt a password for us.
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new super user with given details."""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    # A Docstring
    """Represents a "user profile" inside our system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # 'is active' and 'is_staff' fields are required if we want to override the default user model in Django.
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # Helper functions
    def get_full_name(self):
        """Used to get a user's full name."""

        return self.name

    def get_short_name(self):
        """Used to get a user's short name."""

        return self.name

    def __str__(self):
        """Django uses this when it needs to convert an object to a string."""

        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update."""

    # A field pointing to the user profile, that this update corresponds to.
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string."""

        return self.status_text
