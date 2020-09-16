from django.utils import timezone
from rest_framework import filters
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, UpdateAPIView
from . models import Entrylog
from . serializers import AllEntrySerializer
from main.utils import is_valid_uuid

# All visitors view
class AllEntry(ListAPIView):
    
    serializer_class = AllEntrySerializer
    queryset = Entrylog.objects.all().order_by('-entry_time')   
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__first_name', 'user__phone']





@api_view(['PUT'])
def update_log_entry(request):

    entry_id = request.data.get("entry_id")

    if entry_id is not None:

        # check uui validation
        valid_uuid = is_valid_uuid(entry_id)

        if valid_uuid:

            # Check if entry valid
            try:
                valid_entry = Entrylog.objects.get(id=entry_id)
                # checking checout time is none or exists
                is_checkout = valid_entry.checkout_time

                if is_checkout is None:
                    valid_entry.checkout_time = timezone.now()
                    valid_entry.save()

                    return Response(
                        {
                            "message": "Successfully updated log entry"
                        },
                        status=status.HTTP_200_OK
                    )
                return Response(
                    {
                        "message": "Entrylog already checkout"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )

            except Entrylog.DoesNotExist:
                return Response(
                    {
                        "message": "Entrylog doesn't exists"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )

        return Response(
            {
                "message": "Entry id isn't valid"
            },
            status=status.HTTP_404_NOT_FOUND
        )
    return Response(
        {
            "message": "Entry id is required"
        },
        status=status.HTTP_404_NOT_FOUND
    )
