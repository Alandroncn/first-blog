from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list,name='post_list')
    #path('', views.home, name='home')
    #path(r'^$', views.post_list, name='post_list'),
    #path('', Home.as_view(), name='home')
]