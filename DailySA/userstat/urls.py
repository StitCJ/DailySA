from django.urls import path

from . import views

app_name = 'userstat'

urlpatterns = [
    path('mypage/', views.mypage, name='mypage'),
]