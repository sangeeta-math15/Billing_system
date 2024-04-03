from .models import Bill

from rest_framework import serializers
from .models import Item


class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'price', 'description']


class BillSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'
