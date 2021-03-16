from time import sleep

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView, CreateView, TemplateView, UpdateView
from django.urls import reverse


from account.models import User

from .forms import PixelImageForm
from pixellab import pixel_analyse



class LightCode(LoginRequiredMixin, FormView):
    template_name = 'pixel/ui.html'
    extra_context = {
        'title': 'Image Editor'
    }
    form_class = PixelImageForm

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = self.form_class()
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data()

        if request.is_ajax():
            sleep(3) # Sleeping vaguely
            cloned = request.POST.copy()
            image_name = request.FILES.get('pixel_image').name
            cloned['name'] = image_name

            # Passing the request to form
            form = self.form_class(cloned, request.FILES)

            if form.is_valid():
                image_obj = form.save()

                # Pass the image obj to the pixel analyser to get results
                exif = pixel_analyse(image_obj.image.url)

                if exif:
                    return JsonResponse(exif, status=200)
                else:
                    return JsonResponse({'error': 'This image doesn\'t have any metadata'}, status=400)
            else:
                print(form.errors)
        
        return render(request, self.template_name, context)