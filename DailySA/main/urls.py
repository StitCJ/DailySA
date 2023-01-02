from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('new_post/', views.new_post, name='new_post'),
    path('discussion/', views.discussion, name='discussion'),
    path('<int:discussion_id>/', views.detail, name='detail'),
]