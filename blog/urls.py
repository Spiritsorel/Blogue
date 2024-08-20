
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('contact',contact, name="contact-us"),
    path('posts/', include('posts.urls')),
    path('accounts/', include('users.urls'), name='accounts'),
    path('commentaires/', include('commentaires.urls')),
]


# CRUD