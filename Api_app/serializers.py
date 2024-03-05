
from rest_framework import serializers
from .models import Mainai


class MainaiSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Mainai
        fields = '__all__'