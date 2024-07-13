from django.urls import path

from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [

    path('',views.index, name='index'),


    path('register/', views.register, name='register'),


    # Email verification URL's

    path('email-verification/<str:uidb64>/<str:token>/', views.email_verification, name='email-verification'),


    path('email-verification-sent/', views.email_verification_sent, name='email-verification-sent'),


    path('email-verification-success/', views.email_verification_success, name='email-verification-success'),


    path('email-verification-failed/', views.email_verification_failed, name='email-verification-failed'),


    path('user-logout', views.user_logout, name= 'user-logout'),

    path('profile-management', views.profile_management, name = 'profile-management'),

    path('delete-account', views.delete_account, name = 'delete-account'),


    path('dashboard', views.dashboard, name= 'dashboard'),

    path('account-locked', views.account_locked, name='account-locked'),


  



   # 1 ) Submit our email form

    path('reset_password', auth_views.PasswordResetView.as_view(template_name="secureapp/password/password-reset.html"), name='reset_password'),


    # 2) Success message stating that a password reset email was sent

    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="secureapp/password/password-reset-sent.html"), name='password_reset_done'),


    # 3) Password reset link

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="secureapp/password/password-reset-form.html"), name='password_reset_confirm'),


    # 4) Success message stating that our password was reset

    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="secureapp/password/password-reset-complete.html"), name='password_reset_complete'),



    

  

]





