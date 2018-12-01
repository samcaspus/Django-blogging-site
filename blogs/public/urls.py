from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views

app_name="public"
urlpatterns = [

    url(r'login',views.UserFormViewLogin.as_view(),name="login"),
    url(r'logout',views.logout_view ,name="logout"),

    url(r'register',views.UserFormViewRegister.as_view(),name="register"),

    url(r'delete/(?P<pk>[0-9]+)',views.DeleteBlogs.as_view(),name='delete-blogs'),
    url(r'postblog', views.PostBlogs.as_view(),name='post-blogs'),
    url(r'/',views.IndexView.as_view(), name='index'),
    url(r'',views.IndexView.as_view(), name='index'),
]
