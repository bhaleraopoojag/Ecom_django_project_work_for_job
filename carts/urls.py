
from django.urls import path
from . import views
from carts.views import (cart_home,
                            cart_update,
                            checkout_home,
                            checkout_done_view
                            )
urlpatterns = [

    path('cart_home/',cart_home,name='cart_home'),
    path('cart_update/',cart_update,name='cart_update'),
    path('checkout/',checkout_home,name='checkout'),
    path('checkout/success/',checkout_done_view,name='success'),

]



