from rest_framework import serializers
from mzroad.models import BigData

class Bigdata_Serializer(serializers.ModelSerializer):
    class Meta:
        model = BigData
        fields = '__all__'