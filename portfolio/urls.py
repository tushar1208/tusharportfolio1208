from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),  # Make sure this is correct
    path('admin/', admin.site.urls),
]
