from django.contrib.auth.models import AbstractUser
from django.db import models
from fleet.models import TimeStampedModel, SpaceMap, Unit, Region, Ability, Equipment


# Create your models here.

class Game(TimeStampedModel):
    game_map = models.ForeignKey(
        SpaceMap,
        on_delete=models.DO_NOTHING
    )


class GameProfile(TimeStampedModel):
    name = models.CharField(
        primary_key=True,
        max_length=256,
        unique=True
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.DO_NOTHING
    )
    orders = models.PositiveSmallIntegerField()
    current_order = models.PositiveSmallIntegerField()


class User(AbstractUser):
    profile = models.OneToOneField(
        GameProfile,
        on_delete=models.DO_NOTHING,
        verbose_name="user"
    )


class Action(TimeStampedModel):
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE
    )
    number = models.PositiveSmallIntegerField(
        default=0
    )


class Order(TimeStampedModel):
    order_types = [
        ('ST', "Start"),
        ('MV', 'Move'),
        ('AT', 'Attack'),
        ('DF', 'Defence'),
        ('AB', 'Ability'),
        ('AC', 'Activate'),
    ]
    order_type = models.CharField(
        max_length=2,
        choices=order_types,
        default='ST'
    )
    action = models.ForeignKey(
        Action,
        on_delete=models.CASCADE
    ),
    profile = models.ForeignKey(
        GameProfile,
        on_delete=models.CASCADE
    )
    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE
    )
    target_unit = models.ForeignKey(
        Unit,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    target_region = models.ForeignKey(
        Region,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    target_abil = models.ForeignKey(
        Ability,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    target_equip = models.ForeignKey(
        Equipment,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.profile.name}  order for {self.unit.name} at {self.action}'

    def _attack(self):
        pass

    def _defence(self):
        pass

    def _use_abil(self):
        pass

    def _move(self):
        pass


