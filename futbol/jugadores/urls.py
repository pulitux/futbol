from django.urls import path

from jugadores import views

urlpatterns=[
    path('index',views.index,name='index')
]