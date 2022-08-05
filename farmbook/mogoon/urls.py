from django.urls import path
from . import views
from .views import Home, Notes, Image

urlpatterns = [
    path('/', Home, name='home'),
    path('', Notes, name='notes'),
    path('image/', Image, name='image'),
    path('table/', views.Table, name='mogoon-table'),
    path('update/<int:pk>/', views.update, name='Crop_data-update'),
    path('delete/<int:pk>/', views.delete, name='Crop_data-delete'),
    path('update_form/<int:pk>/', views.update_form, name='Crop_data-update_form'),
]
