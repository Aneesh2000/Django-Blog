from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.blog_form,name='blog_insert'),
    path('<int:id>',views.blog_form,name='blog_update'),
    path('delete/<int:id>/',views.blog_delete,name='blog_delete'),
    path('list/',views.blog_list,name='blog_list')
]