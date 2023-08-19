import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    User model
    """

    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    x_created = models.DateTimeField(auto_now_add=True, editable=False)
    # add more user related fields here

    def __str__(self):
        return self.email
