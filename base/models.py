from django.db import models
import uuid

class BaseModel(models.Model):
    #uuid field
    id         = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    #date fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        abstract = True

