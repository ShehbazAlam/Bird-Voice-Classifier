from django.urls import path, include, re_path
from .views import prediction_list, profile, RegisterView, CustomLoginView, ResetPasswordView, ChangePasswordView
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('prediction-list', prediction_list, name='users-predictions'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='user/login.html',
                                           authentication_form=LoginForm), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),

    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
         name='password_reset_complete'),

    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
]