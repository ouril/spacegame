from uuid import UUID

from django.db import models
from main.models import User, GameProfile, OrderError, Order
from enum import Enum


# Create your models here.

class AttackType(Enum):
    SHOT = 0
    CLOSE = 1
    CRITICAL = 2
    DEAD = 3


class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SpaceMap(TimeStampedModel):
    name = models.CharField(max_length=256, primary_key=True, unique=True)
    description = models.TextField(blank=True, null=True)

    def set_to_dead_location(self, unit: UUID):
        # TODO: Add find to dead location
        pass

    def __str__(self):
        return self.name


class Region(TimeStampedModel):
    is_dead_region = models.BooleanField()
    name = models.CharField(max_length=256, primary_key=True, unique=True)
    description = models.TextField(blank=True, null=True)
    space_map = models.ForeignKey(
        SpaceMap,
        on_delete=models.DO_NOTHING,
        related_name="location"
    )

    def __str__(self):
        return self.pk


class RegionConnection(models.Model):
    region1 = models.ForeignKey(
        Region,
        on_delete=models.DO_NOTHING,
        related_name="connect"
    )
    region2 = models.ForeignKey(
        Region,
        on_delete=models.DO_NOTHING,
        related_name="connect_to_second"
    )

    @staticmethod
    def is_neighbour(location: Region, location_next: Region) -> bool:
        return len(RegionConnection.objects.filter(region1=location.pk, region2=location_next.pk)) > 0

    def __str__(self):
        return self.pk


class UnitClass(models.Model):
    name = models.CharField(unique=True, max_length=256, primary_key=True)

    def __str__(self):
        return self.name


class UnitParams(models.Model):
    health = models.PositiveSmallIntegerField(default=0)
    shields = models.PositiveSmallIntegerField(default=0)
    attack = models.PositiveSmallIntegerField(default=0)
    initiative = models.PositiveSmallIntegerField(default=0)
    speed = models.PositiveSmallIntegerField(default=0)
    unkeep = models.PositiveIntegerField(default=0)
    repair = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.pk


class Unit(TimeStampedModel):
    id = models.UUIDField(unique=True, auto_created=True, primary_key=True)
    name = models.CharField(unique=True, max_length=256)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(
        GameProfile,
        on_delete=models.DO_NOTHING
    )
    params = models.OneToOneField(
        UnitParams,
        on_delete=models.CASCADE,
        related_name="params",
        null=True

    )
    current_params = models.OneToOneField(
        UnitParams,
        on_delete=models.CASCADE,
        related_name="current_params",
        null=True

    )
    type = models.ForeignKey(
        UnitClass,
        on_delete=models.CASCADE,
    )
    location = models.ForeignKey(
        Region,
        on_delete=models.DO_NOTHING,
        related_name='location'
    )
    target_location = models.ForeignKey(
        Region,
        on_delete=models.DO_NOTHING,
        related_name='target_location'
    )

    def set_to_dead(self):
        self.location.space_map.set_to_dead_location(unit=self.id)

    def damage(self, damage: int):
        if self.current_params.health >= damage:
            self.current_params.health = self.current_params.health - damage

        else:
            self.current_params.health = 0

        if self.current_params.health == 0:
            self.set_to_dead()

        self.save()

    def move(self, location: Region, order: Order):
        if RegionConnection.is_neighbour(self.location, location):
            self.location = location
            self.save()
        else:
            error = OrderError(order=order, type_order=Order.order_type, comment="Bad Move! Location not is neighbour")
            error.save()

    def __str__(self):
        return self.name


class Ability(models.Model):
    name = models.CharField(unique=True, max_length=256, primary_key=True)
    on_self = models.BooleanField()
    description = models.TextField(blank=True, null=True)
    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        related_name='abil'
    )


class Equipment(models.Model):
    name = models.CharField(unique=True, max_length=256, primary_key=True)
    description = models.TextField(blank=True, null=True)

    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        related_name="equip"
    )

    def __str__(self):
        return self.name
