from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy, path

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path(
        'password-change/', 
        auth_views.PasswordChangeView.as_view(
                success_url=reverse_lazy('accounts:password_change_done')), 
        name='password-change'
    ),
    path('password-change/done/', 
        auth_views.PasswordChangeDoneView.as_view(), 
        name='password_change_done'
    ),
    path('register/', views.UserRegister.as_view(), name='register'),
    path('register/ajax/validate_username/', views.validate_username, name='validate_username'),
    path('register/ajax/validate_email/', views.register_validate_email, name='register_validate_email'),
    path('edit/', views.UserEdit.as_view(), name='edit'),
    path('edit/ajax/validate_email/', views.edit_validate_email, name='edit_validate_email'),

    path(
        'pwd-reset/', 
        auth_views.PasswordResetView.as_view(
            success_url=reverse_lazy('accounts:pwd_reset_done')), 
        name='password_reset'
    ),
    path('pwd-reset/done', 
        auth_views.PasswordResetDoneView.as_view(),
         name='pwd_reset_done'),
    path(
        'pwd-reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy('accounts:password_reset_complete')),
        name='password_reset_confirm'
    ),
    path(
        'pwd-reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
]
