from django.urls import path
from .views import register_user

urlpatterns = [
    path('register/', view=register_user, name='register'),
]
