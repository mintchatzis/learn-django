#project url routing

from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("",include("hello_app.urls")),
    path('admin/', admin.site.urls)
]

urlpatterns += staticfiles_urlpatterns()