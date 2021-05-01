from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.blog_form),
    path('list/',views.blog_list)
]