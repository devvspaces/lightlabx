from django.db import models


class LightLabImageQuery(models.QuerySet):
	def get_image_by_uuid(self, uuid):
		for i in self:
			if str(i.image_id) == uuid:
				return i 
		return None

class LightLabImageManager(models.Manager):
	def get_queryset(self):
		return LightLabImageQuery(model=self.model, using=self._db)
	def get_image_by_uuid(self, uuid):
		return self.get_queryset().get_image_by_uuid(uuid)
