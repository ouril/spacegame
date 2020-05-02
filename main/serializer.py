from rest_framework import serializers

from main.models import Unit, Game, GameProfile


class UnitsSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Unit
        fields = "__all__"




class GamesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = "__all__"



class PlayersSerializer(serializers.ModelSerializer):

    class Meta:
        model = GameProfile
        fields = "__all__"