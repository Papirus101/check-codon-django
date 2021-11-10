from django.contrib.auth.models import User
from django.db import models


class Dnk(models.Model):
    dnk = models.CharField('Цепочка ДНК', max_length=255)


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    codon = models.CharField('Кодон пользователя', max_length=3)
    approved = models.BooleanField(default=False)
