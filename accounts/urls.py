from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_page, name='register'),
    path('user-page/', views.user_page, name='user-page'),
    path('setting/', views.setting, name='setting'),
]

urlpatterns += [
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'),
         name='reset_password'),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_form.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_done.html'),
         name='password_reset_complete'),
]