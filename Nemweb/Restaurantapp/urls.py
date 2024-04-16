from django.urls import path
from . import views 
urlpatterns = [
    path('', views.home, name='home'),
    path('s', views.aboutus, name='aboutus'),
    path('', views.contact, name='contact'),

]