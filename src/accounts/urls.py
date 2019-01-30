
from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', accounts_views.signup, name='signup'),
    path('password_change/', accounts_views.PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', accounts_views.PasswordChangeDone.as_view(), name='password_change_done'),
]