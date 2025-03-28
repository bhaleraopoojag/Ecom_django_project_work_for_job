"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from accounts.views import login_page,register_page,logout_req,guest_register_view
from address.views import checkout_address_create_view,checkout_address_reuse_view
from . import views 
from carts.views import cart_detail_api_view
from .views import home_page,about_page,contact_page

# from products.views import ProductListView,product_list_view,ProductDetailView,ProductDetailslugView,product_detail_view,ProductFeaturedDetailView,ProductFeaturedListView
urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/",views.home_page,name='home'),
    path('about/',views.about_page,name='about'),
    path('products/', include(("products.urls","products"), namespace='products')),
    path('search/', include(("search.urls","search"), namespace='search')),
    
    path('contact/',views.contact_page,name='contact'),
    path('login/',views.login_page,name='login'),
    path('register/guest',guest_register_view,name='guest_register'),

    path('logout/',views.logout_req,name='logout'),
    path('api/cart/',cart_detail_api_view,name='api-cart'),
    path('cart/', include(("carts.urls","cart"), namespace='cart')),

    path('register/',views.register_page,name='register'),
    path('bootstrap/',TemplateView.as_view(template_name='bootstrap/example.html')),
    path('checkout/address/create/',checkout_address_create_view,name='checkout_address_create'),
    path('checkout/address/reuse/',checkout_address_reuse_view,name='checkout_address_reuse'),

]

if settings.DEBUG:
    urlpatterns = urlpatterns+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


