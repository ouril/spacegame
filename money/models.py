from django.db import models
from fleet.models import TimeStampedModel, Region
from main.models import GameProfile


# Create your models here.


class Resource(TimeStampedModel):
    credits = models.PositiveIntegerField()
    bucta = models.PositiveIntegerField()
    fuel = models.PositiveIntegerField()


class EconomicUnit(TimeStampedModel):
    id = models.UUIDField(primary_key=True, unique=True, auto_created=True)
    name = models.CharField(
        max_length=256
    )
    user = models.ForeignKey(
        GameProfile,
        on_delete=models.DO_NOTHING
    )
    description = models.TextField(blank=True, null=True)
    profit = models.ForeignKey(
        Resource,
        on_delete=models.CASCADE

    )
    is_regular = models.BooleanField(
        default=False
    )
    region = models.ForeignKey(
        Region,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.name
