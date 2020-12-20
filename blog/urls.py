from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('secret_page/', views.secret_page, name='secret_page')
]