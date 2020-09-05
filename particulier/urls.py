from django.urls import path

from particulier.views import particulier_views

app_name = 'particulier'

urlpatterns = [
    path('', particulier_views, name='particulier_home')
]
