from django.urls import path
from .views import registerCarStore, deleteCarStore

urlpatterns = [
    path('register/', registerCarStore, name="registerCarStore"),
    path('carstore/delete/', deleteCarStore, name='delete_carstore'),
]
