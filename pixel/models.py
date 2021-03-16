import uuid

from django.db import models


class LightLabImage(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='light_lab_images/')
    image_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )

    def __str__(self):
        return f'LightLabImage {self.name}'