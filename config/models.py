from django.db import models


# Create your models here.

class TurnLevel(models.Model):
    name = models.CharField(max_length=128, default="Неизвестно")
    initiative = models.PositiveIntegerField(default=0)
    is_used = models.BooleanField(default=False)
