from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('post_property/', views.post_property, name='post_property'),
    path('my_properties/', views.my_properties, name='my_properties'),
    path('properties/', views.property_list, name='property_list'),
    path('properties/<int:pk>/', views.property_detail, name='property_detail'),
    path('properties/<int:pk>/like/', views.like_property, name='like_property'),
]
