"""slmwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import permission
import registration
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework.routers import DefaultRouter
from helloslmapp.views import (helloworld,
                               AuthHomePageView,
                               HomePageView,)
permission.autodiscover()
api_router = DefaultRouter()
# api_router.register(r'helloworld', HomePageView.as_view())

urlpatterns = [
    url(r'^mygoogauth/', include("social_django.urls", namespace="social")),
    url(r'^index\.html', TemplateView.as_view(template_name='index.html')),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^helloview$', HomePageView.as_view(), name='HelloViewIsMyName'),
    url(r'^authhello$', AuthHomePageView.as_view(), name='AuthenticHello'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logmein/$', auth_views.login, name='login'),
    url(r'^api/', include(api_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework'))
]

# Django doesn't get requests for static assets in production, however, in dev
# mode, we just let Django serve our static content. We use
# staticfiles_urlpatterns in urls.py to tell Django to serve requests
# for static/*.
if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL,
                           document_root=settings.STATIC_ROOT,
                           show_indexes=True)
urlpatterns += staticfiles_urlpatterns()
