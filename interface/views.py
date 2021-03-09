from django.shortcuts import render


def home(request):
    context = {
        'title': 'Image Editing Tool',
    }

    return render(request, 'interface/index.html', context)

def about(request):
    context = {
        'title': 'About Us',
    }

    return render(request, 'interface/about.html', context)

def gallery(request):
    context = {
        'title': 'Example Gallery',
    }

    return render(request, 'interface/gallery.html', context)

def freepresets(request):
    context = {
        'title': 'Free Lightroom Preset - Download',
    }

    return render(request, 'interface/freepresets.html', context)

def lightroompresets(request):
    context = {
        'title': 'Learn to create any look you want',
    }

    return render(request, 'interface/lightroompresets.html', context)

def presetfinder(request):
    context = {
        'title': 'Lightroom Preset Finder',
    }

    return render(request, 'interface/preset_finder.html', context)

def resources(request):
    context = {
        'title': 'Resources',
    }

    return render(request, 'interface/resources.html', context)

def faq(request):
    context = {
        'title': 'Frequently Asked Questions (FAQ)',
    }

    return render(request, 'interface/faq.html', context)


def find_photo_with_metadata(request):
    context = {
        'title': 'How to Find Photos with Metadata',
    }

    return render(request, 'interface/find_photo_data.html', context)

def insta_data(request):
    context = {
        'title': 'How to Get Metadata for Instagram Photos',
    }

    return render(request, 'interface/insta_data.html', context)