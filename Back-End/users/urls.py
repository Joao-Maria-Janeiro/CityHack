from django.urls import path, include
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('create_division/', views.create_division, name="create_division"),
    path('login/', views.login_view, name="login"),
    path('', views.user_page, name="user_page"),
]
