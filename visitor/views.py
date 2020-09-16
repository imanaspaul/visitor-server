from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from . models import Visitor
from entrylog.models import Entrylog
from . serializers import AllVisitorSerializer


# All visitors view
class AllVisitor(ListAPIView):
    
    serializer_class = AllVisitorSerializer
    queryset = Visitor.objects.all()

    # Search filter
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'phone']



# Create visitor
@api_view(['POST'])
def create_visitor(request):

    # Getting the data
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    phone = request.data.get("phone")
    
    # checing the first name is provided or not
    if first_name == None:
        return Response({
                "message": "First name is requred!"
            },
            status=status.HTTP_403_FORBIDDEN
        )
    if last_name == None:
        return Response({
                "message": "Last name is requred!"
            },
            status=status.HTTP_403_FORBIDDEN
        )
    if phone == None:
        return Response({
                "message": "Phone number is requred!"
            },
            status=status.HTTP_403_FORBIDDEN
        )

    # checking if visitor already exists
    is_visitor = Visitor.objects.filter(first_name=first_name, phone=phone)
    if is_visitor.exists():
        # Checcking if the user alredy inside the apartement
        is_visiting = Entrylog.objects.filter(user__first_name=first_name, checkout_time=None)
        if is_visiting.exists():
            return Response({
                    "message": "User with this credential already inside the apartement!"
                },
                status=status.HTTP_403_FORBIDDEN
            )
        user = is_visitor[0]
        # creating the log entry with existing vistor
        add_log_entry = Entrylog.objects.create(user=user)
        add_log_entry.save()
        return Response({
                    "message": "Successfully added log entry"
                },
                status=status.HTTP_201_CREATED
        )

    # Creating the visitor
    visitor = Visitor.objects.create(
        first_name=first_name,
        last_name=last_name,
        phone=phone
    )
    add_log_entry = Entrylog.objects.create(user=visitor)
    add_log_entry.save()
    return Response({
                    "message": "Successfully added log entry"
                },
                status=status.HTTP_201_CREATED
        )