from django.urls import path
from .views import register_user, login_user, check_email, check_nickname

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name="login_user"),
    path('check_email/', check_email, name='check_email'),
    path('check_nickname/', check_nickname, name='check_email'),
]
