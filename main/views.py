from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from main.models import Unit
from .serializer import UnitsSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class UnitViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Unit.objects.all()
        serializer = UnitsSerializer(queryset, many=True)
        return Response(serializer.data)