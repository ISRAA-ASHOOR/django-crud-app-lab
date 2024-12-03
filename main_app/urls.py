from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('fishs/', views.fish_index, name='fish-index'),
    path('fishs/<int:fish_id>/', views.fish_detail, name='fish-detail'),
]