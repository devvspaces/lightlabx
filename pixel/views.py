from time import sleep
import logging
import json

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse, Http404, HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView, CreateView, TemplateView, UpdateView
from django.urls import reverse
from django.template.loader import render_to_string


from account.models import User

from .forms import PixelImageForm, AddImageForm
from .utils import simplify, random_text
from .models import Gallery, LightLabImage

from pixellab import pixel_analyse


# Set the loggers
debugger = logging.getLogger('dev')
choke = logging.getLogger('dev.error')


# Admin add image view
class AddImage(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = 'pixel/addimage.html'
    extra_context = {
        'title': 'Add Gallery Image',
        'view_id': 'gallery',
    }
    form_class = AddImageForm

    def test_func(self):
        if self.request.user.is_admin:
            return True
        return False

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = self.form_class()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()

        # Passing the request to form
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            image_obj = form.save()

            messages.success(request, 'A new image as been added')

            return redirect('gallery')
        else:
            print(form.errors)
        
        return render(request, self.template_name, context)



class LightCode(LoginRequiredMixin, FormView):
    template_name = 'pixel/ui.html'
    extra_context = {
        'title': 'Image Editor',
        'view_id': 'account',
    }
    form_class = PixelImageForm


    def process_image(self, image_obj):
        # Pass the image obj to the pixel analyser to get results
        exif = pixel_analyse(image_obj.image.url)

        # Take the camera name and model and add them together
        # Make + Model
        if exif:
            exif['Camera Model'] = f"{exif.get('Make')} {exif.get('Model')}"
            exif["ExposureTime"] = simplify(exif["ExposureTime"])

        return exif

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = self.form_class()

        # Lets see if there are some arguments in the kwargs
        slugid = self.kwargs.get('slugid')

        # debugger.debug(slugid)
        if slugid:
            # Meaning a gallery image was clicked
            # Get the image_obj or 404
            image_obj = get_object_or_404(Gallery, slugid=slugid)

            # Check if the image_obj has any metadata
            if len(image_obj.meta_data) < 10:
                # Get the exif data and pass to the context in a list
                exif = self.process_image(image_obj)

                # Add the image slug id to the exif
                exif['image_id'] = image_obj.slugid

                # Lets dump this data as json
                json_str = json.dumps(exif)

                # Add the json str to the obj
                image_obj.meta_data = json_str
                image_obj.save()
            else:
                json_str = image_obj.meta_data

            context['exif'] = json_str

            # Also send the image link to the context
            context['image_link'] = image_obj.image.url

        # We have to get the little images for quick try examples
        little_images = Gallery.objects.all()[:4]
        context['little_images'] = little_images

        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data()

        if request.is_ajax():
            cloned = request.POST.copy()
            image_name = request.FILES.get('pixel_image').name
            cloned['name'] = image_name

            # Passing the request to form
            form = self.form_class(cloned, request.FILES)

            if form.is_valid():
                image_obj = form.save()

                # Process the image which returns the exif data
                exif = self.process_image(image_obj)

                # Add the image id to the exif
                exif['image_id'] = str(image_obj.image_id)

                # Also add the lightroom settings to the same dict when you get it

                # Lets dump this data as json to save to the model
                json_str = json.dumps(exif)
                image_obj.meta_data = json_str
                image_obj.save()

                if exif:
                    return JsonResponse(exif, status=200)
                else:
                    return JsonResponse({'error': ['This image doesn\'t have any metadata']}, status=400)
            else:
                print(form.errors)
        
        return render(request, self.template_name, context)



class AutoGenerated(LoginRequiredMixin, TemplateView):
    template_name = 'pixel/addimage.html'
    extra_context = {
        'title': 'Image Editor',
        'view_id': 'account',
    }

    def get(self, request, *args, **kwargs):
        # Get the image_id from the kwargs
        image_id = self.kwargs.get('image_id')
        return_type = self.kwargs.get('return_type')

        if image_id and return_type:
            # Get the image obj
            # Let's differentiate btw a gallery image and user uploaded image by their identifiers
            if image_id.find('-') == -1:
                # Meaning this is a gallery image
                image_obj = Gallery.objects.filter(slugid=image_id).first()
            else:
                image_obj = LightLabImage.objects.get_image_by_uuid(image_id)

            if image_obj:
                meta_dict = dict()
                try:
                    # Covert to json string to dictionary
                    meta_dict = json.loads(image_obj.meta_data)
                except json.decoder.JSONDecodeError:
                    pass

                if return_type == 'lrtemplate':
                    template = "pixel/format.lrtemplate"
                    file_name = f'{random_text()}.lrtemplate'
                elif return_type == 'xmp_raw':
                    template = "pixel/format_raw.xmp"
                    file_name = f'{random_text()} - raw.xmp'
                elif return_type == 'xmp_extended':
                    template = "pixel/format_extended.xmp"
                    file_name = f'{random_text()} - extended.xmp'
                else:
                    return HttpResponseNotFound(content='The page you are requesting for does not exist')

                message=render_to_string(template,meta_dict)

                # print(message)

                if request.is_ajax():
                    return JsonResponse({'file_name': file_name, 'file_data': message}, status=200)
                return HttpResponse(content=message)

        # Call a 404 error page instead
        return HttpResponseNotFound(content='The page you are requesting for does not exist')