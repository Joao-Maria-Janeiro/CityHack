from django.urls import path, include
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('register_plug/', views.register_plug, name="register_plug"),
    # path('update_waste/', csrf_exempt(views.update_waste), name="update_waste"),
    # path('set_monthly_budget/', csrf_exempt(views.set_monthly_budget), name="set_monthly_budget"),
]
