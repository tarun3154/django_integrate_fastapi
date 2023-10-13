from django.contrib import admin
from django.urls import path, include
from fastapi_app.main import app as fastapi_app
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userprofile.urls')),
    path('', fastapi_app)
]
