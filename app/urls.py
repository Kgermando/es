from django.urls import path

from app.views import home_views, contact_views, about_views

app_name = 'app'

urlpatterns = [
    path('', home_views, name='home'),
    path('contact', contact_views, name='contact'),
    path('about', about_views, name='about')
]
