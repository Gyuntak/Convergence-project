from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import BigData
from .bigData_serializers import Bigdata_Serializer
from .AI_serializers import AI_Serializer
from django.shortcuts import redirect
from mzroad.process_bigdata import process_bigdata

@api_view(['GET'])
def getData(req):
    bigData = BigData.objects.all()
    serializer = Bigdata_Serializer(bigData,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addData(req):
    serializer = Bigdata_Serializer(data = req.data)

    if serializer.is_valid():
        serializer.save()

    return redirect("http://127.0.0.1:8000/bigData")

@api_view(['GET'])
def bigData(req):

    bigdata = BigData.objects.all()
    serializer = Bigdata_Serializer(bigdata, many=True)

    return Response(process_bigdata(serializer.data))