from django.urls import path

from entreprise.views import entreprise_home

app_name = 'entreprise'

urlpatterns = [
    path('', entreprise_home, name='entreprise_home'),
]
