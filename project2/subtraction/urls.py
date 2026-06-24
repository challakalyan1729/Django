
from django.urls import path
from subtraction import views
urlpatterns = [
    path('Sub/',views.subtraction),
    path('Mul/',views.multiplication)
]