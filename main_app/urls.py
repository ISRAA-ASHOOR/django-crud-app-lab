from django.urls import path
from . import views 

urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('fishs/', views.fish_index, name='fish-index'),
    path('fishs/<int:fish_id>/', views.fish_detail, name='fish-detail'),
    path('fishs/create/', views.FishCreate.as_view(), name='fish-create'),
    path('fishs/<int:pk>/update/', views.FishUpdate.as_view(), name='fish-update'),
    path('fishs/<int:pk>/delete/', views.FishDelete.as_view(), name='fish-delete'),
    path('fishs/<int:fish_id>/add-feeding/', views.add_feeding, name='add-feeding'),
]