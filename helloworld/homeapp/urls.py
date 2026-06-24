from django.urls import path
from homeapp.views import fun,fun2,fun3
urlpatterns = [
    path('', fun),
    path('page1/', fun2),
    path('page2/', fun3)
]