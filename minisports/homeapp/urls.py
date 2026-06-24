from django.urls import path
from homeapp.views import fun,create_event,events
urlpatterns = [
    path('',fun),
    path('create/',create_event),
    path('events/',events)
]