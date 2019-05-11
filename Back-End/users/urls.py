from django.urls import path, include
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('signup/', csrf_exempt(views.signup_view), name="signup"),
    path('create_division/', csrf_exempt(views.create_division), name="create_division")
]
