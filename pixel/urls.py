from django.urls import path,include

from . import views
urlpatterns = [
    path('light_editor/', views.LightCode.as_view(), name='lightcode'),
]