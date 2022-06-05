#converts the objects into data types that are understandable by
# javascript and front-end frameworks. 

from django.db.models import fields
from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('category', 'subcategory', 'name', 'amount')
        