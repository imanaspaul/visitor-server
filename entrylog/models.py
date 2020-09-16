import uuid
from django.db import models
from visitor.models import Visitor


# Entry log models
class Entrylog(models.Model):

    id = models.UUIDField( 
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False)
    user = models.ForeignKey(Visitor, related_name="entry", on_delete=models.CASCADE)
    entry_time = models.DateTimeField(auto_now_add=True, verbose_name="Vistor entry date and time")
    checkout_time = models.DateTimeField(verbose_name="Vistor checkout date and time", blank=True, null=True)
    purpose = models.TextField(verbose_name="Purpose of visit")

    def __str__(self):
        return self.user.first_name
    