from django.db import models

from django.contrib.auth.models import User as BaseUser

from .utils import UserGenders


class User(BaseUser):
    gender = models.SmallIntegerField(choices=UserGenders.choices(), default=UserGenders.MALE)

    class Meta:
        db_table = "users"
