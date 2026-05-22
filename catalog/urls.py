from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.catalog_view, name='catalog'),
    path('part/<int:part_id>/', views.part_detail, name='part_detail'),
]