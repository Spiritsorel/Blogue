from django.urls import path
from .views import *

urlpatterns = [
    path('publication/<int:pk>/', publication_detail, name='publication_detail')
]
