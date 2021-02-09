from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import CustomerLoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
urlpatterns = [

    # ---------------------------All For Home Page-----------------------------------------
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    
    path('laptop/', views.laptop, name='laptop'),   
    path('laptop/<slug:data>', views.laptop, name='laptopdata'),

    path('topweare/', views.topweare, name='topweare'),
    path('bottomweare/', views.bottomweare, name='bottomweare'),

    # ---------------------------Registration Login Reset Pass-----------------------------------------
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    
    #logout required some page after logout so in Setting.py it mentions LOGIN_REDIRECT_URL = '/profile/'
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',
                                             authentication_form=CustomerLoginForm), name='login'),
    
    # next Page must mentions so that it get redirect
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', 
            form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    
    #After Password Change it should redirect to somewhere
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view
                (template_name='app/passwordchangedone.html'), name='passwordchangedone'),


    #Password Reset
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class= MySetPasswordForm), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name="password_reset_complete"),


    #Profile View
    path('profile/', views.ProfileView.as_view(), name='profile'),

    # Add To cart
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='show_cart'),

# AJAX
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),


    path('paymentdone/', views.payment_done, name='paymentdone'),

    path('buy/', views.buy_now, name='buy-now'),

    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),



    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

