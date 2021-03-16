from django import forms
from django.core.validators import validate_email
from django.contrib.auth import password_validation
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404

from .models import LightLabImage



class PixelImageForm(forms.Form):
    name = forms.CharField(max_length=255, required=False)
    pixel_image = forms.ImageField()

    def save(self, commit=True):
        # Get all the required information
        image = self.cleaned_data.get('pixel_image')
        name = self.cleaned_data.get('name')

        # Creating the LightImage obj
        image_obj = LightLabImage(image=image, name=name)

        if commit:
            image_obj.save()
        
        return image_obj