from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from public import urls

urlpatterns = [
    url('admin', admin.site.urls),
    url('',include('public.urls')),
]
