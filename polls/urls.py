from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('enter/', views.enter, name='enter'),
    path('<login>/', views.user_info, name='user_info'),
]