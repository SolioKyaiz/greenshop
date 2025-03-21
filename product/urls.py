from django.urls import path
from .views import *

urlpatterns = [
    path('',PlantListAPIView.as_view(),name = 'plant_list'),
    path('create/',PlantCreateAPIView.as_view(),name = 'plant_create'),
    path('update/<int:id>/',PlantUpdateAPIView.as_view(),name = 'plant_update'),
    path('delete/<int:id>/',PlantDeleteAPIView.as_view(),name = 'plant_delete'),
    path('<int:id>/',PlantDetailAPIView.as_view(),name = 'plant_detail'),

    path('detail-delete/<int:id>/',PlantDetailDeleteAPIView.as_view(),name = 'plant_detail_delete'),
    path('list-create/',PlantListCreateAPIView.as_view(),name = 'plant_list_create'),
    path('detail-update-delete/<int:id>/',PlantDetailUpdateDeleteAPIView.as_view(),name = 'plant_detail_update_delete'),
]