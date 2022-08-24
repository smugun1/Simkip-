from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', Home, name='home'),

    path('sign_up/', views.Sign_Up_Table, name='mogoon-sign_up_table'),
    path('sign_in/', views.Sign_In_Table, name='mogoon-sign_in_table'),
    path('logout/', views.Logout, name='mogoon-logout_table'),

    path('crop_table/', views.CropTable, name='mogoon-crop_table'),
    path('crop_table_update/', views.CropTableUpdate, name='mogoon-crop_table_update'),
    path('crop_create/', views.mogoonCropCreate, name='mogoon-crop_create'),

    path('kandojobs_table/', views.KandojobsTable, name='mogoon-kandojobs_table'),
    path('kandojobs_table_update/', views.KandojobsTableUpdate, name='mogoon-kandojobs_table_update'),
    path('kandojobs_create/', views.mogoonKandojobsCreate, name='mogoon-kandojobs_create'),

    path('fertilizer_table/', views.FertilizerTable, name='mogoon-fertilizer_table'),
    path('fertilizer_table_update/', views.mogoonFertilizerTableCreate, name='mogoon-fertilizer_table_update'),
    path('fertilizer_create/', views.mogoonFertilizerCreate, name='mogoon-fertilizer_create'),

    path('milk_table/', views.MilkTable, name='mogoon-milk_table'),
    path('milk_table_update/', views.MilkTableUpdate, name='mogoon-milk_table_update'),
    path('milk_create/', views.mogoonMilkCreate, name='mogoon-milk_create'),

    path('update/<int:pk>/', views.update, name='Crop_data-update'),
    path('delete/<int:pk>/', views.delete, name='Crop_data-delete'),

]
