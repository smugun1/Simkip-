from django.urls import path
from . import views
from .views import Home, Crop_Table_Update

urlpatterns = [
    path('/', Home, name='home'),
    path('crop_table_update/', Crop_Table_Update, name='crop_table_update'),
    path('sign_up/', views.Sign_Up_Table, name='mogoon-sign_up_table'),
    path('sign_in/', views.Sign_In_Table, name='mogoon-sign_in_table'),
    path('crop_table/', views.Crop_Table, name='mogoon-crop_table'),
    path('kandojobs_table/', views.KandojobsTable, name='mogoon-kandojobs_table'),
    path('milk_table/', views.MilkTable, name='mogoon-milk_table'),
    path('create/', views.mogoonCreate, name='mogoon-create'),
    path('update/<int:pk>/', views.update, name='Crop_data-update'),
    path('delete/<int:pk>/', views.delete, name='Crop_data-delete'),

]
