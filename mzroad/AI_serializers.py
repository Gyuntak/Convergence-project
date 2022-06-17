from rest_framework import serializers
from mzroad.models import BigData
from mzroad.models import AI
from rest_framework import serializers
from mzroad.models import AI

class AI_Serializer(serializers.ModelSerializer):
    class Meta:
        model = AI
        fields = '__all__'