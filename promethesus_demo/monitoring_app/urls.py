
from django.urls import path
from . import views

urlpatterns = [
    # Main endpoints
    path('', views.home_view, name='home'),
    path('user/profile/', views.user_profile, name='user_profile'),
    path('search/', views.search_api, name='search_api'),
    
    # Performance testing endpoints
    path('compute/', views.heavy_computation, name='heavy_computation'),
    path('upload/', views.file_upload, name='file_upload'),
    path('analytics/', views.analytics_data, name='analytics_data'),
    
    # Utility endpoints
    path('health/', views.health_check, name='health_check'),
    path('loadtest/', views.load_test, name='load_test'),
]