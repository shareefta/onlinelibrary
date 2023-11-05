from django.urls import path
from . import views

urlpatterns = [
    path('',views.library,name="library"),
    path('content/',views.content,name="content")
]