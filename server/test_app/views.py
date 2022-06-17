from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from test_app.models import Test
from test_app.serializers import TestSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()

    serializer_class = TestSerializer

@api_view(['GET'])
def bigData(req):
    test = Test.objects.all()
    serializer = TestSerializer(test, many=True)
  