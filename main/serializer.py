from rest_framework import serializers

from main.models import Unit


class UnitsSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Unit
        fields = "__all__"