from django.urls import path
from . import views
from .views import *

# from django.conf.urls import patterns, url

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
    path('fertilizer_table_update/', views.mogoonFertilizerTableUpdate,
         name='mogoon-fertilizer_table_update'),
    path('fertilizer_create/', views.mogoonFertilizerCreate, name='mogoon-fertilizer_create'),

    path('milk_table/', views.MilkTable, name='mogoon-milk_table'),
    path('milk_table_update/', views.MilkTableUpdate, name='mogoon-milk_table_update'),
    path('milk_create/', views.mogoonMilkCreate, name='mogoon-milk_create'),

    path('update/<int:pk>/', views.update, name='Crop_data-update'),
    path('delete/<int:pk>/', views.delete, name='Crop_data-delete'),
    path('f_update/<int:pk>/', views.F_update, name='fertilizer-update'),
    path('f_delete/<int:pk>/', views.F_delete, name='fertilizer-delete'),
    path('k_update/<int:pk>/', views.K_update, name='kandojobs-update'),
    path('k_delete/<int:pk>/', views.K_delete, name='kandojobs-delete'),
    path('m_update/<int:pk>/', views.M_update, name='milk-update'),
    path('m_delete/<int:pk>/', views.M_delete, name='milk-delete'),

]
