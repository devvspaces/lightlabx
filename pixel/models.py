import uuid

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .utils import get_usable_slug
from .managers import LightLabImageManager


class LightLabImage(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='light_lab_images/')
    image_id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )
    meta_data = models.TextField(blank=True)
    created = models.DateField(auto_now=True)

    objects = LightLabImageManager()

    def __str__(self):
        return f'LightLabUserUpload {self.name}'


class Gallery(models.Model):
    slugid = models.SlugField(max_length=16, unique=True, editable=False)
    image = models.ImageField(upload_to='gallery_images/')
    meta_data = models.TextField(blank=True)

    # class Meta:
    # 	verbose

    def __str__(self):
        return f'LightLabImage {self.slugid}'



@receiver(pre_save, sender=Gallery)
def post_save_create_membership(sender, instance, **kwargs):
    if not instance.slugid:
        new_slug = get_usable_slug(instance)
        instance.slugid = new_slug