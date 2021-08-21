from django.urls import path
from accounts.views import login_view, logout_view, register_view
from accounts.profile import UserDetailView

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('user/<int:pk>/profile/', UserDetailView.as_view(), name='user_profile')
    ]