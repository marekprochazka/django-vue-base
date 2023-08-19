import uuid
from typing import Iterable

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    x_created = models.DateTimeField(auto_now_add=True)
    x_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-x_created"]

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def save(
            self,
            force_insert: bool = False,
            force_update: bool = False,
            using: str | None = None,
            update_fields: Iterable[str] | None = None,
            update_metadata_fields: bool = True,
    ):
        # https://code.djangoproject.com/ticket/30319  , https://code.djangoproject.com/ticket/22981
        fields = update_fields
        if update_fields and update_metadata_fields:
            fields = set(update_fields)
            fields.update(["x_modified"])
        return super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=fields,
        )
