from django.urls import path
from addition import views
urlpatterns = [
    path('addition/',views.add)
]