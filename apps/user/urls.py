from django.urls import path

from . import views


app_name = 'user'


urlpatterns = [
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('identitycertification/', views.IdentityCertificationView.as_view(), name='identitycertification'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard')
]
