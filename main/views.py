from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from main.models import Unit, Game, GameProfile
from .serializer import UnitsSerializer, PlayersSerializer, GamesSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class UnitViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Unit.objects.all()
        serializer = UnitsSerializer(queryset, many=True)
        return Response(serializer.data)


class PlayersViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = GameProfile.objects.all()
        serializer = PlayersSerializer(queryset, many=True)
        return Response(serializer.data)


class GameViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Game.objects.all()
        serializer = GamesSerializer(queryset, many=True)
        return Response(serializer.data)
