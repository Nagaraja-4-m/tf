from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login,name='admin_login'),
    path('register', views.register,name='admin_register'),
    path('logout', views.logout,name='admin_logout'),
    path('', views.dashboard,name='admin_dashboard'),
    path('products', views.products,name='admin_productpage'),
    path('products/<int:pid>', views.product_update,name='product_action'),
    path('site', views.site_update,name='admin_sitepage'),
    path('social-media', views.socialmedia_contact_update,name='admin_socialmedia_contact_page'),
]
