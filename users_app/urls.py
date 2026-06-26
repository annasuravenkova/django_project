from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from users_app.views import ProfileDetailView, ProfileUpdateView, CustomLoginView
from django.contrib.auth.views import (
         PasswordResetView, PasswordResetDoneView,
         PasswordResetConfirmView, PasswordResetCompleteView
     )

app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(template_name='users/password_change.html', success_url=reverse_lazy('users:password_change_done')), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),name='password_change_done'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html', email_template_name='users/password_reset_email.html', success_url=reverse_lazy('users:password_reset_done')), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html', success_url=reverse_lazy('users:password_reset_complete')), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
