from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('travel', views.travel),
    path('addplan', views.addplan),
    path('createplan', views.createplan),
    path('show/<travel_id>', views.show),
    path('join/<travel_id>', views.join),
    path('logout', views.logout),
    path('delete/<id>', views.delete)
]