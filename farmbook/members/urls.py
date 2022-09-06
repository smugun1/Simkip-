from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.sign_up, name='signup'),
    # path('user_login/', views.user_login, name='login'),
    path('user_login/', auth_views.LoginView.as_view(template_name='authenticate/userlogin.html'), name='login'),
    path('user_logout/', auth_views.LoginView.as_view(template_name='authenticate/userlogout.html'), name='logout'),
    path('profile/', views.user_profile, name='profile'),
    # path('logout/', views.user_logout, name='logout'),
    path('', include('mogoon.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
