from django.conf.urls import include, url
from django.contrib import admin
from .views import home as home_view

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^books_cbv/', include('books_cbv.urls', namespace='books_cbv')),
    url(r'^$', home_view)
]
