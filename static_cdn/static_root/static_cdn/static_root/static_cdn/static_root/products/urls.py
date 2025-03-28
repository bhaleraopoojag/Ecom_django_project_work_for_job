
from django.urls import path
from . import views
from products.views import (ProductListView,
                            ProductDetailslugView,
                            )
urlpatterns = [

    path('',ProductListView.as_view(),name='list'),
    path('<slug:slug>/',ProductDetailslugView.as_view(),name='detail'),
]



