from rest_framework import serializers
from . models import Visitor

# Visitor serialzer
class AllVisitorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visitor
        fields = ['id', 'first_name', 'last_name', 'phone']