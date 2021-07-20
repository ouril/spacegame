import uuid
from decimal import Decimal
from enum import Enum

from django.contrib.auth.models import User
from django.db import models

# from .admin_models import TimeStampedModel, SpaceMap, Unit, Region, Ability, Equipment
from config.models import TurnLevel

DEAD_LOCATION = "dead_location"

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


class TimeStampedModel(models.Model):
    # id = models.UUIDField(
    #     primary_key=True,
    #     auto_created=True,
    #     default=uuid.uuid4()
    # )

    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
        # managed = False


class SpaceMap(models.Model):
    id = models.UUIDField(
        primary_key=True,
        auto_created=True,
        default=uuid.uuid4()
    )
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    id = models.UUIDField(
        primary_key=True,
        auto_created=True,
        default=uuid.uuid4()
    )
    name = models.CharField(
        max_length=256,
        # unique=True,
        default="",
        primary_key=False,
        null=True,
        blank=True
    )
    created_on = models.DateTimeField(auto_now_add=True, null=True, primary_key=False, )
    game_map = models.ForeignKey(
        SpaceMap,
        on_delete=models.DO_NOTHING,
        default=None,
        primary_key=False,
        null=True,
        related_name="game"
    )
    is_in_process = models.BooleanField(default=False, primary_key=False, )
    is_in_archive = models.BooleanField(default=False, primary_key=False, )

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (('name', 'id', 'game_map', 'is_in_process', 'created_on',),)


class GameProfile(TimeStampedModel):
    id = models.UUIDField(
        auto_created=True,
        primary_key=True,
        default=uuid.uuid4()
    )
    name = models.CharField(
        max_length=256,
        primary_key=False,
        default="",
        blank=True
        # unique=True
    )
    game = models.ForeignKey(
        Game,
        default=None,
        on_delete=models.DO_NOTHING,
        null=True,
        primary_key=False,
        blank=True
    )
    #
    user = models.OneToOneField(
        User,
        primary_key=False,
        default=None,
        null=True,
        on_delete=models.DO_NOTHING
    )
    orders = models.PositiveSmallIntegerField(default=0)
    current_order = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        # pass
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=256, primary_key=True, unique=True)
    description = models.TextField(blank=True, null=True)
    space_map = models.ForeignKey(
        SpaceMap,
        primary_key=False,
        on_delete=models.DO_NOTHING,
        related_name="location",
        db_constraint=False
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


class Unit(TimeStampedModel):
    # uuid = models.UUIDField(unique=True, auto_created=True, primary_key=True, blank=True, null=False)
    name = models.CharField(unique=True, max_length=256)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(
        GameProfile,
        on_delete=models.DO_NOTHING
    )

    type = models.ForeignKey(
        UnitClass,
        on_delete=models.CASCADE,
    )
    location = models.ForeignKey(
        Region,
        on_delete=models.DO_NOTHING,
        related_name='location',
        null=True,
        blank=True
    )
    target_location = models.ForeignKey(
        Region,
        on_delete=models.DO_NOTHING,
        related_name='target_location',
        null=True,
        blank=True
    )
    pic = models.ImageField(
        blank=True,
        null=True
    )

    def set_to_dead(self):
        self.location = Region.objects.get(name=DEAD_LOCATION)
        self.save()

    # def damage(self, damage: int):
    #     if self.current_params.health >= damage:
    #         self.current_params.health = self.current_params.health - damage
    #
    #     else:
    #         self.current_params.health = 0
    #
    #     if self.current_params.health == 0:
    #         self.set_to_dead()

    # self.save()

    # def move(self, location: Region, order: Order):
    #     if RegionConnection.is_neighbour(self.location, location):
    #         self.location = location
    #         self.save()
    #     else:
    #         error = OrderError(order=order, type_order=Order.order_type, comment="Bad Move! Location not is neighbour")
    #         error.save()

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
    current = models.BooleanField(default=False)
    unit: Unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        related_name="params",
        null=True

    )

    def __str__(self):
        if self.unit != None:
            return f"UnitParams {self.unit} current: {self.current}"
        return f"UnitParams {self.id}"


class UnitType(models.Model):
    name = models.CharField(max_length=256, unique=True)
    desc = models.TextField(max_length=2048, blank=True, default="")
    unit = models.ManyToManyField(
        Unit,
        related_name="unittype",
        default=None,
        blank=True,
        null=True,
    )


class Ability(models.Model):
    name = models.CharField(unique=True, max_length=256, primary_key=True)
    on_self = models.BooleanField()
    description = models.TextField(blank=True, null=True)
    unit = models.ManyToManyField(
        Unit,
        default=None,
        blank=True,
        null=True,
        related_name='abil'

    )

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(unique=True, max_length=256, primary_key=True)
    description = models.TextField(blank=True, null=True)

    unit = models.ManyToManyField(
        Unit,
        related_name="equip",
    )

    def __str__(self):
        return self.name


# class OrderType(Enum):
#     ENTER = "ST"
#     DEFENSE = "DF"
#     ABILITY = "AB"
#     ATTACK = "AT"
#     MOVE = "MV"
#     ACTIVATE = "AC"


# class User(AbstractUser):
#     profile = models.OneToOneField(
#         GameProfile,
#         on_delete=models.DO_NOTHING,
#         related_name="user"
#     )
#
#     def __str__(self):
#         return self.username


class Action(TimeStampedModel):
    game = models.ForeignKey(
        Game,
        default=None,
        null=True,
        on_delete=models.CASCADE
    )
    number = models.PositiveSmallIntegerField(
        default=0
    )

    def __str__(self):
        return f"{self.game.name} action {self.number}"


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
        blank=True,
        related_name='order_target'
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
    turn_level = models.OneToOneField(
        TurnLevel,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None
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

    # def fulfill_order(self):
    #     if self.order_type == self.AB:
    #         self._use_abil()
    #     elif self.order_type == self.AC:
    #         self._activate()
    #     elif self.order_type == self.AT:
    #         self._attack()
    #     elif self.order_type == self.ST:
    #         self._start()
    #     elif self.order_type == self.DF:
    #         self._defence()
    #     elif self.order_type == self.MV:
    #         self._move()


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


class Resource(TimeStampedModel):
    credits = models.PositiveIntegerField()
    bucta = models.PositiveIntegerField()
    fuel = models.PositiveIntegerField()


class EconomicUnit(TimeStampedModel):
    # id = models.UUIDField(primary_key=True, unique=True, auto_created=True)
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


class AttackBuf(models.Model):
    attack_type = models.OneToOneField(AttackType, on_delete=models.DO_NOTHING)
    simple_buf = models.SmallIntegerField(default=0)
    simple_kf = models.DecimalField(max_digits=4, decimal_places=2, default=Decimal('1.00'))

    def full_buf(self):
        pass


class SpecialBuff(models.Model):
    target_type = models.OneToOneField(
        UnitType, on_delete=models.DO_NOTHING
    )
    plus = models.SmallIntegerField(default=0)
    kf = models.DecimalField(max_digits=4, decimal_places=2, default=Decimal('1.00'))
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
