from django.contrib import admin
from django.urls import path, include
from manipulation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('manipulation.urls')),
]
