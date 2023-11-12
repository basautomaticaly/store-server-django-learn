from django.contrib.auth.decorators import login_required
from django.urls import path

from users.views import UserProfileView, UserRegistrationView, login, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', logout, name='logout'),
]
