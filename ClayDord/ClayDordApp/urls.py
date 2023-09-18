from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.homePage, name = 'home'),
    path('shop/',views.shopPage,name = 'shop'),
    path('signin/',views.signInPage,name = 'signin'),
    path('signup/',views.signUpPage,name = 'signup'),
    path('cart/',views.cartPage,name = 'cart'),

    #Forget Password paths
    path('reset_password',auth_views.PasswordResetView.as_view(template_name = 'password_reset.html'), name = 'reset_password'),
    path('password_reset_done',auth_views.PasswordResetDoneView.as_view(),name = 'password_reset_done'),
    path('password/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(),name = 'password_reset_complete')
]


 
