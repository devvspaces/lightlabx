from django.shortcuts import render

from pixel.models import Gallery


def home(request):
    context = {
        'title': 'Image Editing Tool',
        'view_id': 'home',
    }

    return render(request, 'interface/index.html', context)

def about(request):
    context = {
        'title': 'About Us',
        'view_id': 'about',
    }

    return render(request, 'interface/about.html', context)

def gallery(request):
    context = {
        'title': 'Example Gallery',
        'view_id': 'gallery',
    }

    # Get all the gallery images and pass them to the context
    context['images'] = Gallery.objects.all()

    return render(request, 'interface/gallery.html', context)

def freepresets(request):
    context = {
        'title': 'Free Lightroom Preset - Download',
        'view_id': 'resources',
    }

    return render(request, 'interface/freepresets.html', context)

def lightroompresets(request):
    context = {
        'title': 'Learn to create any look you want',
        'view_id': 'resources',
    }

    return render(request, 'interface/lightroompresets.html', context)

def presetfinder(request):
    context = {
        'title': 'Lightroom Preset Finder',
        'view_id': 'presetfinder',
    }

    return render(request, 'interface/preset_finder.html', context)

def resources(request):
    context = {
        'title': 'Resources',
        'view_id': 'resources',
    }

    return render(request, 'interface/resources.html', context)

def faq(request):
    context = {
        'title': 'Frequently Asked Questions (FAQ)',
        'view_id': 'faq',
    }

    return render(request, 'interface/faq.html', context)


def find_photo_with_metadata(request):
    context = {
        'title': 'How to Find Photos with Metadata',
        'view_id': 'resources',
    }

    return render(request, 'interface/find_photo_data.html', context)

def insta_data(request):
    context = {
        'title': 'How to Get Metadata for Instagram Photos',
        'view_id': 'resources',
    }

    return render(request, 'interface/insta_data.html', context)