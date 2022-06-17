from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Test
from .serializers import TestSerializer
from django.shortcuts import redirect
from test_app.process_bigdata import process_bigdata

@api_view(['GET'])
def getData(req):
    test = Test.objects.all()
    serializer = TestSerializer(test,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addData(req):
    serializer = TestSerializer(data = req.data)
    if serializer.is_valid():
        serializer.save()
    return redirect("http://127.0.0.1:8000/bigData")

@api_view(['GET'])
def bigData(req):
    test = Test.objects.all()
    serializer = TestSerializer(test, many=True)

    return Response(process_bigdata(serializer.data))