from django.contrib import admin
from django.urls import path
# Combined imports for cleaner code
from table.views import display_student, find_result, home

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Added the 'name' argument to each path (Highly Recommended)
    path('display/',display_student,name='display_student'),
    path('find/', find_result, name='find_result'),
    path('home/', home, name='home_page'),
]