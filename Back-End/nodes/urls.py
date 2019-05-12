from django.urls import path, include
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('register_plug/', views.register_plug, name="register_plug"),
    path('daily_rundown/<slug:division_name>/', views.daily_rundown, name="daily_rundown"),
    path('associate_member/', views.associate_member, name="associate_member"),
    path('member_waste/<slug:member_name>/',views.member_waste, name ="member_waste")
    # path('product_rundown/<slug:division_name>/<slug:product_name>/', views.product_rundown, name="product_rundown"),
    # path('update_waste/', csrf_exempt(views.update_waste), name="update_waste"),
    # path('set_monthly_budget/', csrf_exempt(views.set_monthly_budget), name="set_monthly_budget"),
]
