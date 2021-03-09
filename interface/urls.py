from django.urls import path,include

from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('gallery-photos/', views.gallery, name='gallery'),
    path('free-lightroom-presets-download/', views.freepresets, name='freepreset'),
    path('lightroom-presets/', views.lightroompresets, name='lightroompresets'),
    path('lightroom-preset-finder/', views.presetfinder, name='presetfinder'),
    path('resources/', views.resources, name='resources'),
    path('faq/', views.faq, name='faq'),
    path('about/', views.about, name='about'),
    path('find-photo-with-metadata/', views.find_photo_with_metadata, name='find_photo_with_metadata'),
    path('how-to-get-metadata-from-instagram/', views.insta_data, name='insta_data'),
]