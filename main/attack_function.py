from fleet.models import Order

from django.db import models
from fleet.models import TimeStampedModel, SpaceMap, Unit, Region, Ability, Equipment, UnitType
from main.models import OrderType, ORDER_TYPE


class AttackType(models.Model):
    name = models.CharField(max_length=256, unique=True)
    desc = models.TextField(max_length=2048, blank=True, default="")
    unit = models.ForeignKey(
        Unit,
        on_delete=models.DO_NOTHING,
        related_name="attacktype"
    )

    def attack(self, unit):
        pass


class AttackBuf(models.Model):
    attack_type = models.OneToOneField(AttackType, on_delete=models.DO_NOTHING)
    simple_buf = models.SmallIntegerField(default=0)

    def full_buf(self):
        pass


class SpecialBuff(models.Model):
    target_type = models.OneToOneField(
        UnitType, on_delete=models.DO_NOTHING
    )
    plus = models.SmallIntegerField(default=0)
    kf = models.DecimalField(max_digits=4, decimal_places=2)
    attack_type = models.ForeignKey(
        AttackBuf,
        on_delete=models.DO_NOTHING,
        related_name="special"
    )

    def buf(self):
        pass


class SpecialEffect(models.Model):
    BLANK = "BLANK"
    START = "START"
    NEAR = "NEAR_"
    choice = (
        (START, "START"),
        (NEAR, "NEAR"),
        (BLANK, "BLANK")
    )
    lose_attack = models.PositiveSmallIntegerField(default=0)
    move_effect = models.CharField(max_length=5, choices=choice, default=BLANK)
    target_type = models.OneToOneField(
        UnitType, on_delete=models.DO_NOTHING
    )
    attack_type = models.ForeignKey(
        AttackBuf,
        on_delete=models.DO_NOTHING,
        related_name="effect"
    )
    deactivate = models.CharField(max_length=2, choices=ORDER_TYPE, null=True, blank=True)

    def use(self, unit: Unit):
        pass

