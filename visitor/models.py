import uuid
from django.db import models

# Visitors models ( User details )
class Visitor(models.Model):

    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False) 
    first_name = models.CharField(max_length=255, verbose_name="First Name")
    last_name = models.CharField(max_length=255, verbose_name="Last Name")
    phone = models.CharField(max_length=12)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    