from django.contrib import admin
from .models import *
# from .admin_models import *
from django.contrib.auth.admin import UserAdmin


# admin.site.register(User, UserAdmin)
# Register your models here.s
# @admin.register(OrderType)
# class OrderTypeAdmin(admin.ModelAdmin):
#     pass


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     pass


@admin.register(GameProfile)
class GameProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderError)
class OrderErrorAdmin(admin.ModelAdmin):
    pass


@admin.register(SpaceMap)
class SpaceMapAdmin(admin.ModelAdmin):
    pass


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(RegionConnection)
class RegionConnectionAdmin(admin.ModelAdmin):
    pass


@admin.register(UnitClass)
class UnitClassAdmin(admin.ModelAdmin):
    pass


@admin.register(UnitParams)
class UnitParamsAdmin(admin.ModelAdmin):
    pass


@admin.register(Unit)
class UnitParamsAdmin(admin.ModelAdmin):
    pass


@admin.register(TurnLevel)
class TurnLevelParamsAdmin(admin.ModelAdmin):
    pass


@admin.register(UnitType)
class UnitTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Ability)
class AbilityAdmin(admin.ModelAdmin):
    pass


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    pass
