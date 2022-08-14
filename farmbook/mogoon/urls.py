from django.urls import path
from . import views
from .views import Home, Notes, Image

urlpatterns = [
    path('/', Home, name='home'),
    path('', Notes, name='notes'),
    path('table/', views.Table, name='mogoon-table'),
    path('create/', views.mogoonCreate, name='mogoon-create'),
    path('update/<int:pk>/', views.update, name='Crop_data-update'),
    path('delete/<int:pk>/', views.delete, name='Crop_data-delete'),

]
