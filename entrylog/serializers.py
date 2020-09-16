from rest_framework.serializers import ModelSerializer
from visitor.serializers import AllVisitorSerializer
from . models import Entrylog

# Visitor serialzer
class AllEntrySerializer(ModelSerializer):

    user = AllVisitorSerializer()

    class Meta:
        model = Entrylog
        fields =  [
            "id",
            "entry_time",
            "checkout_time",
            "purpose",
            "user"
        ]
        
        # depth = 1