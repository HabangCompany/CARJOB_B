from django.urls import path
from .views import registerCarStore

urlpatterns = [
    path('register/', registerCarStore, name="registerCarStore")
]
