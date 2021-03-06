"""es URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('app.urls')),
    path('accounts/', include('accounts.urls')),
    path('particulier/', include('particulier.urls')),
    path('entreprise/', include('entreprise.urls')),
    path('ourteam/', include('ourteam.urls')),
    path('admin/', admin.site.urls),
]

handler400 = 'handlers.views.handler400'
handler403 = 'handlers.views.handler403'
handler404 = 'handlers.views.handler404'
handler500 = 'handlers.views.handler500'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
