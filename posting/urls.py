from django.urls import path
from . import views

urlpatterns = [
    path('posting/', views.posting, name='posting'),
    path('instagram/', views.instagram, name='instagram'),
    path('contact/', views.contact, name='contact'),
]