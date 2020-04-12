from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models
from fleet.models import TimeStampedModel, SpaceMap, Unit, Region, Ability, Equipment
from main.attack_function import AttackType


class OrderType(Enum):
    ENTER = "ST"
    DEFENSE = "DF"
    ABILITY = "AB"
    ATTACK = "AT"
    MOVE = "MV"
    ACTIVATE = "AC"


ST = "ST"
MV = "MV"
AT = "AT"
DF = "DF"
AB = "AB"
AC = "AC"

ORDER_TYPE = (
        (ST, "Start"),
        (MV, 'Move'),
        (AT, 'Attack'),
        (DF, 'Defence'),
        (AB, 'Ability'),
        (AC, 'Activate'),
    )


class Game(TimeStampedModel):
    name = models.CharField(
        primary_key=True,
        max_length=256,
        unique=True
    )
    game_map = models.ForeignKey(
        SpaceMap,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name


class User(AbstractUser):
    profile = models.OneToOneField(
        GameProfile,
        on_delete=models.DO_NOTHING,
        related_name="user"
    )

    def __str__(self):
        return self.username


class Action(TimeStampedModel):
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE
    )
    number = models.PositiveSmallIntegerField(
        default=0
    )

    def __str__(self):
        return f"{self.game.name} action {self.number}"


class Order(TimeStampedModel):
    order_type = models.CharField(
        max_length=2,
        choices=ORDER_TYPE,
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
    attack_type = models.ForeignKey(
        AttackType,
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

    def _start(self):
        pass

    def _activate(self):
        pass

    def fulfill_order(self):
        if self.order_type == self.AB:
            self._use_abil()
        elif self.order_type == self.AC:
            self._activate()
        elif self.order_type == self.AT:
            self._attack()
        elif self.order_type == self.ST:
            self._start()
        elif self.order_type == self.DF:
            self._defence()
        elif self.order_type == self.MV:
            self._move()


class OrderError(TimeStampedModel):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="error"
    )

    type_order = models.PositiveSmallIntegerField(default=0)
    comment = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return f'Error {self.order.unit.name} in {self.order.action} {self.type_order}'
