from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view

import json

from main.models import Unit, Game, GameProfile
from main.rpc_utils import JsonRPCData
from .serializer import UnitsSerializer, PlayersSerializer, GamesSerializer
from rest_framework import viewsets
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def turn(request):
    """

    {
    "jsonrpc": "2.0",
    "method": "STOP",
    "params":["stop"],
    "id": 1
    }

    :param request:
    :return:
    """

    if request.method == "POST":
        data = request.data
        print(data)
        rpc = JsonRPCData(data)
        if rpc.method == JsonRPCData.STOP:
            rpc.set_result({'res': True})
        res = rpc.get_rpc_result()
        print(res)
        if res[0]:
            return Response(res[1])
        return Response({"done": True})

    return Response({
        "jsonrpc": "2.0",
        "methods": {
            JsonRPCData.STOP: ['<game.name>'],
            JsonRPCData.CALC: {
                JsonRPCData.MethodKeys.GAME_NAME: '<game.name>',
                JsonRPCData.MethodKeys.GAME_ACT: '<action.number>'
            },
            JsonRPCData.START: ['<game.name>'],
            JsonRPCData.TURN: {
                JsonRPCData.MethodKeys.GAME_NAME: '<game.name>',
                JsonRPCData.MethodKeys.TURN_ACT: ['start', 'stop', 'remote']

            },
        }
    })


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
