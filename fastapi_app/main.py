import os
import django
django.setup()
from fastapi import FastAPI
from django.conf import settings
from asgiref.sync import sync_to_async
from userprofile.models import UserProfiles
from fastapi.middleware.wsgi import WSGIMiddleware
from django.core.wsgi import get_wsgi_application

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django_app = get_wsgi_application()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_integrate_fastapi.settings')

app = FastAPI()

sync_get_user_data = sync_to_async(UserProfiles.objects.all)



@app.get("/api/get-data")
async def get_user_data():
    user_profiles = await sync_get_user_data()

    # Prepare the user data to be sent as JSON
    user_data = []
    for profile in user_profiles:
        user_data.append({
            "username": profile.user.username,
            "email": profile.user.email,
            "address": profile.address,
            "phone": profile.phone,
        })

    return {"user_profiles": user_data}


app.mount('/', WSGIMiddleware(django_app))