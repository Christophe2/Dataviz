from django.db import models
from django.contrib.auth.models import AbstractUser

from cerberus_ac.models import RoleMixin


class User(AbstractUser, RoleMixin):
    email_confirmed = models.BooleanField(default=False)


class ShinyApp(models.Model):
    pass
